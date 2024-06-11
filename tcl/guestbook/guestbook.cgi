#!/bin/sh
# guestbook.cgi
# Implements a simple guestbook page.
# The set of visitors is kept in a simple database.
# The newguest.cgi script will update the database
# \
exec tclsh "$0" ${1+"$@"}

# The guestbook.data file has the database
# The file is in the same directory as the script.

set dir [file dirname [info script]]
set datafile [file join $dir guestbook.data]

# Load our supporting Tcl procedures to define Cgi_Header
source [file join $dir cgihacks.tcl]
Cgi_Header "Vishal's Guestbook"

if {![file exists $datafile]} {
    puts "No registered guests, yet.
        <P>
        Be the first
        <A href='newguest.html'>Register</A>"
} else {
    puts "The following folks have registered in my Guestbook.
        <P>
        <A href='newguest.html'>Register</A>
        <H2>Guests</H2>"
    catch {source $datafile}
    foreach name [lsort [array names Guestbook]] {
        set item $Guestbook($name)
        set homepage [lindex $item 0]
        set markup [lindex $item 1]
        puts "<H3><A href=$homepage>$name</A></H3>
        puts $markup
    }
}
puts "</BODY></HTML>"