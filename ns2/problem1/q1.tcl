#!/usr/bin/tclsh8.6

#Create a simulator object
set ns [new Simulator]

#dynamic routing
$ns rtproto DV

#Open the NAM trace file
set nf [open q1.nam w]
$ns namtrace-all $nf


#finish method
proc finish {} {
 global ns
 $ns flush-trace
 exit 0
}

#Creatint 100 nodes
for {set i 0} {$i < 50} {incr i} {
set n($i) [$ns node]
}

#10 nodes communicating in loop i.e. droping the packets
for {set i 0} {$i < 10} {incr i} {
$ns duplex-link $n($i) $n([expr ($i+1)%10]) 1Mb 10ms DropTail
}


#Call the finish procedure after 5 seconds of simulation time
$ns at 5.0 "finish"
#Run the simulation
$ns run
