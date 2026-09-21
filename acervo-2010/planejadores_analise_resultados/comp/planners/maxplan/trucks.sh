



i=1
while [ $i -le 9 ]
do

rm ff_temp -f
rm CG_temp -f 

echo "solving Trucks problem #$i"

./maxplan  -problem /home/cic/rh11/domains/Trucks/Propositional/Strips/p0$i.pddl  -cgproblem /home/cic/rh11/domains/Trucks/Propositional/p0$i.pddl -domain /home/cic/rh11/domains/Trucks/Propositional/Strips/domain_p0$i.pddl -cgdomain "/home/cic/rh11/domains/Trucks/Propositional/domain.pddl" -timeout 9600 -londexMode 2 >trucks_result$i




i=`expr $i + 1`
done



i=10
while [ $i -le 30 ]
do



rm ff_temp -f
rm CG_temp -f 

echo "solving Trucks problem #$i"

./maxplan  -problem "/home/cic/rh11/domains/Trucks/Propositional/Strips/p$i.pddl"  -cgproblem "/home/cic/rh11/domains/Trucks/Propositional/p$i.pddl" -domain "/home/cic/rh11/domains/Trucks/Propositional/Strips/domain_p$i.pddl" -cgdomain "/home/cic/rh11/domains/Trucks/Propositional/domain.pddl" -timeout 9600 -londexMode 2 -londexm 1 >trucks_result$i





i=`expr $i + 1`
done


rm solverout* -f
rm original* -f 
rm CG_Temp -f 
rm ff_Temp -f 
#rm *_result* -f 
