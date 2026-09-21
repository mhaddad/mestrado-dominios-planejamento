



i=1
while [ $i -le 9 ]
do

rm ff_temp -f
rm CG_temp -f 

echo "solving SATELLITE problem #$i"

./maxplan  -problem "/home/cic/rh11/domains/SATELLITE/STRIPS/P0$i.PDDL"  -cgproblem "/home/cic/rh11/domains/SATELLITE/STRIPS/P0$i.PDDL" -domain "/home/cic/rh11/domains/SATELLITE/STRIPS/DOMAIN.PDDL" -cgdomain "/home/cic/rh11/domains/SATELLITE/STRIPS/DOMAIN.PDDL"  -globaltime 120 -londexMode 2  >satellite_result$i




i=`expr $i + 1`
done



i=10
while [ $i -le 30 ]
do



rm ff_temp -f
rm CG_temp -f 

echo "solving SATELLITE problem #$i"

./maxplan  -problem "/home/cic/rh11/domains/SATELLITE/STRIPS/P$i.PDDL"  -cgproblem "/home/cic/rh11/domains/SATELLITE/STRIPS/P$i.PDDL" -domain "/home/cic/rh11/domains/SATELLITE/STRIPS/DOMAIN.PDDL" -cgdomain "/home/cic/rh11/domains/SATELLITE/STRIPS/DOMAIN.PDDL"  -globaltime 120 -londexMode 2 >satellite_result$i



i=`expr $i + 1`
done


rm solverout* -f
rm original* -f 
rm CG_Temp -f 
rm ff_Temp -f 
#rm *_result* -f 
