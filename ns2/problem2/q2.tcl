#!/usr/bin/tclsh8.6

## varianle declearation
set val(chan) Channel/WirelessChannel
set val(prop) Propagation/TwoRayGround
set val(netif) Phy/WirelessPhyExt
set val(mac) Mac/802_11Ext
set val(ifq) Queue/DropTail/PriQueue
set val(ll) LL
set val(ant) Antenna/OmniAntenna
set val(ifqlen) 250
set val(nn) 100
set val(rp) DumbAgent
set val(x) 200
set val(y) 200

#Create a simulator object
set ns [new Simulator]

#Open the a trace file
set tracef [open q2.tr w]
$ns trace-all $tracef

#nam trace fole for wireless
set nf [open q2.nam w]
$ns namtrace-all-wireless $nf $val(x) $val(y)

#Create Topography
set topo [new Topography]
$topo load_flatgrid $val(x) $val(y)

#create God
create-god $val(nn)
set chan_ [new $val(chan)]

$ns node-config -adhocRouting $val(rp) -llType $val(ll) \
-macType $val(mac) -ifqType $val(ifq) \
-ifqLen $val(ifqlen) -antType $val(ant) \
-propType $val(prop) -phyType $val(netif) \
-topoInstance $topo a-agentTrace ON \
-routerTrace ON -macTrace ON \
-movementTrace ON -channel $chan_

for {set i 0} {$i<$val(nn)} {incr i} {
set n($i) [$ns node]
$n($i) random-motion 0
}

for {set i 0} {$i<50} {incr i} {
$n($i) set X_ 5.0
$n($i) set Y_ 2.0
$n($i) set Z_ 0.0

$n([expr 99-$i]) set X_ 390.0
$n([expr 99-$i]) set Y_ 385.0
$n([expr 99-$i]) set Z_ 0.0
}


# Req for nam
for {set i 0} {$i < 10} {incr i} {
$ns at 0.0 "$n(${i}) setdest [$n(${i}) set X_] [$n(${i}) set Y_] 0.0"
}

set tcp [new Agent/TCP]
set sink [new Agent/TCPSink]
$ns attach-agent $n(0) $tcp
$ns attach-agent $n(1) $sink
$ns connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp

proc stop {} {
global ns tracef nf
$ns flush-trace
close $tracef; close $nf
exec nam q2 &
exit 0
}
$ns at 0.5 "$ftp start"
$ns at 5.0 "$ftp stop"
$ns at 6.0 "stop"
$ns run






