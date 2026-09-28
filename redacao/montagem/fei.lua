--[[
Filtro do Pandoc para o padrão da FEI (redacao/README.md, "Padrão da FEI").

- Citação entre parênteses com o sobrenome em maiúsculas, como na versão de 2010: "(HELMERT, 2006)";
  a citação no fluxo do texto fica como está: "Helmert (2006)".
- Tabelas numeradas: "Tabela 1 – Título" (identificação em cima). Tabela dentro de ::: quadro ::: vira
  "Quadro 1 – Título".
- Figuras: "Figura 1 – Título" em cima da imagem (o Pandoc põe a legenda embaixo).
- ::: fonte ::: aplica o estilo "Fonte" (fonte 10, embaixo da ilustração ou tabela).
- Títulos com a classe .pretextual (RESUMO, ABSTRACT, listas, SUMÁRIO) viram parágrafo centralizado,
  fora do sumário. Títulos .unnumbered continuam no sumário, sem número (REFERÊNCIAS, APÊNDICE).
- ::: {.campo #sumario} ::: (e #ilustracoes, #tabelas, #quadros) vira um marcador que montar.py troca
  pelo campo do Word correspondente.

Roda depois do --citeproc (a ordem dos filtros na linha de comando importa).
]]

local n_tabela, n_figura, n_quadro = 0, 0, 0

local minusculas = { ["et"] = true, ["al."] = true, ["al.,"] = true, ["al.;"] = true, ["p."] = true,
  ["apud"] = true, ["cap."] = true, ["v."] = true, ["f."] = true }

local function maiusculas_na_citacao(el)
  if #el.citations == 0 or el.citations[1].mode ~= "NormalCitation" then
    return nil
  end
  local depois_do_ano = false
  el.content = el.content:walk({
    Str = function(s)
      local t = s.text
      if t:match("%d%d%d%d") then
        -- depois do ano vem o localizador (p. 34) ou o próximo autor, depois de ";"
        depois_do_ano = not t:match(";$")
        return nil
      end
      if depois_do_ano or minusculas[t] then
        return nil
      end
      return pandoc.Str(pandoc.text.upper(t))
    end,
  })
  return el
end

local function prefixar(blocos, rotulo)
  local inl = pandoc.utils.blocks_to_inlines(blocos)
  local novo = pandoc.Inlines({ pandoc.Str(rotulo), pandoc.Space(), pandoc.Str("–"), pandoc.Space() })
  novo:extend(inl)
  return novo
end

local function numerar_tabela(tbl, tipo)
  local rotulo
  if tipo == "quadro" then
    n_quadro = n_quadro + 1
    rotulo = "Quadro " .. n_quadro
  else
    n_tabela = n_tabela + 1
    rotulo = "Tabela " .. n_tabela
  end
  if #tbl.caption.long > 0 then
    tbl.caption.long = { pandoc.Plain(prefixar(tbl.caption.long, rotulo)) }
  end
  return tbl
end

return {
  {
    Cite = maiusculas_na_citacao,
  },
  {
    Div = function(div)
      if div.classes:includes("quadro") then
        return div:walk({ Table = function(t) return numerar_tabela(t, "quadro") end })
      end
      if div.classes:includes("fonte") then
        div.attributes["custom-style"] = "Fonte"
        return div
      end
      if div.classes:includes("campo") then
        return pandoc.Para({ pandoc.Str("@@CAMPO:" .. div.identifier .. "@@") })
      end
    end,
  },
  {
    Table = function(t)
      if t.caption.long and #t.caption.long > 0 then
        local primeiro = pandoc.utils.stringify(t.caption.long)
        if primeiro:match("^Quadro %d") then
          return nil
        end
      end
      return numerar_tabela(t, "tabela")
    end,
    Figure = function(fig)
      n_figura = n_figura + 1
      local titulo = pandoc.Div({ pandoc.Para(prefixar(fig.caption.long, "Figura " .. n_figura)) },
        { ["custom-style"] = "Legenda de figura" })
      local corpo = fig.content:walk({
        Image = function(img)
          img.caption = {}
          return img
        end,
      })
      local blocos = pandoc.Blocks({ titulo })
      blocos:extend(corpo)
      return blocos
    end,
    Header = function(h)
      if h.classes:includes("pretextual") then
        return pandoc.Div({ pandoc.Para(h.content) }, { ["custom-style"] = "Titulo sem numero" })
      end
    end,
  },
}
