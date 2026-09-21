



i=1
while [ $i -le 20 ]
do

rm ff_temp -f
rm CG_temp -f 

echo "solving driverslog #$i"

./maxplan    -problem ~/domains/DriverLog/Strips/pfile$i  -cgproblem ~/domains/DriverLog/Strips/pfile$i -domain ~/domains/DriverLog/Strips/driverlog.pddl -cgdomain ~/domains/DriverLog/Strips/driverlog.pddl -timeout 7200 -londexMode 2  >driverlog_result$i




i=`expr $i + 1`
done



#i=10
#while [ $i -le 30 ]
#do



#irm ff_temp -f
#rm CG_temp -f 


#./maxplan   -path ~/domains/Trucks/Propositional/Strips/ -problem "p$i.pddl"  -cgproblem "../p$i.pddl" -domain "domain_p$i.pddl" -cgdomain "../domain.pddl" -timeout 1800 -solver minisat >trucks_result$i





#i=`expr $i + 1`
#done


rm solverout* -f
rm original* -f 
rm CG_Temp -f 
rm ff_Temp -f 
#rm *_result* -f 
