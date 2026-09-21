



i=1
while [ $i -le 9 ]
do

rm ff_temp -f
rm CG_temp -f 

echo "solving Pipesworld_ipc5 problem #$i"

./maxplan  -problem "/home/cic/rh11/domains/Pipesworld_ipc5/Propositional/p0$i.pddl"  -cgproblem "/home/cic/rh11/domains/Pipesworld_ipc5/Propositional/p0$i.pddl" -domain "/home/cic/rh11/domains/Pipesworld_ipc5/Propositional/domain.pddl" -cgdomain "/home/cic/rh11/domains/Pipesworld_ipc5/Propositional/domain.pddl"  -globaltime 120 -londexMode 2 >pipesworld_result$i




i=`expr $i + 1`
done



i=10
while [ $i -le 50 ]
do



rm ff_temp -f
rm CG_temp -f 

echo "solving Pipesworld_ipc5 problem #$i"

./maxplan  -problem "/home/cic/rh11/domains/Pipesworld_ipc5/Propositional/p$i.pddl"  -cgproblem "/home/cic/rh11/domains/Pipesworld_ipc5/Propositional/p$i.pddl" -domain "/home/cic/rh11/domains/Pipesworld_ipc5/Propositional/domain.pddl" -cgdomain "/home/cic/rh11/domains/Pipesworld_ipc5/Propositional/domain.pddl"  -globaltime 120 -londexMode 0 >pipesworld_result$i



i=`expr $i + 1`
done


rm solverout* -f
rm original* -f 
rm CG_Temp -f 
rm ff_Temp -f 
#rm *_result* -f 
