#############################################################################
# Generated by PAGE version 4.23a
#  in conjunction with Tcl version 8.6
#  Jun 18, 2019 01:24:25 PM CEST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font9
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#
    menu .pop46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font {{Segoe UI} 9} -foreground black \
        -tearoff 1 
    vTcl:DefineAlias ".pop46" "Popupmenu1" vTcl:WidgetProc "" 1

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -relief raised -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor {#000000} 
    wm focusmodel $top passive
    wm geometry $top 834x738+541+145
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3844 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Ping Pong Ding Dong"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    labelframe $top.lab51 \
        -font TkDefaultFont -foreground black -text {PID Controls} \
        -background {#d9d9d9} -height 155 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 160 
    vTcl:DefineAlias "$top.lab51" "Labelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab51
    scale $site_3_0.sca64 \
        -activebackground {#ececec} -background {#d9d9d9} -bigincrement 0.0 \
        -font TkTextFont -foreground {#000000} -from 0.0 \
        -highlightbackground {#d9d9d9} -highlightcolor black -length 116 \
        -orient horizontal -resolution 1.0 -tickinterval 0.0 -to 100.0 \
        -troughcolor {#d9d9d9} 
    vTcl:DefineAlias "$site_3_0.sca64" "Scale1" vTcl:WidgetProc "Toplevel1" 1
    scale $site_3_0.sca65 \
        -activebackground {#ececec} -background {#d9d9d9} -bigincrement 0.0 \
        -font TkTextFont -foreground {#000000} -from 0.0 \
        -highlightbackground {#d9d9d9} -highlightcolor black -length 116 \
        -orient horizontal -resolution 1.0 -tickinterval 0.0 -to 100.0 \
        -troughcolor {#d9d9d9} 
    vTcl:DefineAlias "$site_3_0.sca65" "Scale2" vTcl:WidgetProc "Toplevel1" 1
    scale $site_3_0.sca67 \
        -activebackground {#ececec} -background {#d9d9d9} -bigincrement 0.0 \
        -font TkTextFont -foreground {#000000} -from 0.0 \
        -highlightbackground {#d9d9d9} -highlightcolor black -length 116 \
        -orient horizontal -resolution 1.0 -tickinterval 0.0 -to 100.0 \
        -troughcolor {#d9d9d9} 
    vTcl:DefineAlias "$site_3_0.sca67" "Scale3" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes68 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Kp \
        -width 18 
    vTcl:DefineAlias "$site_3_0.mes68" "Message4" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes69 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Ki \
        -width 20 
    vTcl:DefineAlias "$site_3_0.mes69" "Message5" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes70 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Kd \
        -width 20 
    vTcl:DefineAlias "$site_3_0.mes70" "Message6" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.sca64 \
        -in $site_3_0 -x 30 -y 100 -anchor nw -bordermode ignore 
    place $site_3_0.sca65 \
        -in $site_3_0 -x 30 -y 60 -anchor nw -bordermode ignore 
    place $site_3_0.sca67 \
        -in $site_3_0 -x 30 -y 20 -anchor nw -bordermode ignore 
    place $site_3_0.mes68 \
        -in $site_3_0 -x 10 -y 40 -width 18 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes69 \
        -in $site_3_0 -x 10 -y 80 -width 20 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes70 \
        -in $site_3_0 -x 10 -y 120 -width 20 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $top.lab52 \
        -font TkDefaultFont -foreground black -text {Servo offsets} \
        -background {#d9d9d9} -height 155 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 160 
    vTcl:DefineAlias "$top.lab52" "Labelframe2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab52
    message $site_3_0.mes57 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text {#1} \
        -width 20 
    vTcl:DefineAlias "$site_3_0.mes57" "Message1" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes58 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text {#2} \
        -width 17 
    vTcl:DefineAlias "$site_3_0.mes58" "Message2" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes59 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text {#3} \
        -width 17 
    vTcl:DefineAlias "$site_3_0.mes59" "Message3" vTcl:WidgetProc "Toplevel1" 1
    scale $site_3_0.sca43 \
        -activebackground {#ececec} -background {#d9d9d9} -bigincrement 0.0 \
        -font TkTextFont -foreground {#000000} -from -20.0 \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -orient horizontal -resolution 1.0 -tickinterval 0.0 -to 20.0 \
        -troughcolor {#d9d9d9} 
    vTcl:DefineAlias "$site_3_0.sca43" "Scale4" vTcl:WidgetProc "Toplevel1" 1
    scale $site_3_0.sca44 \
        -activebackground {#ececec} -background {#d9d9d9} -bigincrement 0.0 \
        -font TkTextFont -foreground {#000000} -from -20.0 \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -orient horizontal -resolution 1.0 -tickinterval 0.0 -to 20.0 \
        -troughcolor {#d9d9d9} 
    vTcl:DefineAlias "$site_3_0.sca44" "Scale5" vTcl:WidgetProc "Toplevel1" 1
    scale $site_3_0.sca45 \
        -activebackground {#ececec} -background {#d9d9d9} -bigincrement 0.0 \
        -font TkTextFont -foreground {#000000} -from -20.0 \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -orient horizontal -resolution 1.0 -tickinterval 0.0 -to 20.0 \
        -troughcolor {#d9d9d9} 
    vTcl:DefineAlias "$site_3_0.sca45" "Scale6" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.mes57 \
        -in $site_3_0 -x 10 -y 40 -width 20 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes58 \
        -in $site_3_0 -x 10 -y 80 -width 17 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes59 \
        -in $site_3_0 -x 10 -y 120 -width 17 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.sca43 \
        -in $site_3_0 -x 30 -y 100 -anchor nw -bordermode ignore 
    place $site_3_0.sca44 \
        -in $site_3_0 -x 30 -y 60 -anchor nw -bordermode ignore 
    place $site_3_0.sca45 \
        -in $site_3_0 -x 30 -y 20 -anchor nw -bordermode ignore 
    labelframe $top.lab53 \
        -font TkDefaultFont -foreground black -text {Connection Status} \
        -background {#d9d9d9} -height 75 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 160 
    vTcl:DefineAlias "$top.lab53" "Labelframe3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab53
    label $site_3_0.lab57 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#1dc104} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -relief ridge \
        -text Connected 
    vTcl:DefineAlias "$site_3_0.lab57" "Label1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab57 \
        -in $site_3_0 -x 10 -y 20 -width 140 -relwidth 0 -height 45 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $top.lab43 \
        -font TkDefaultFont -foreground black -text States \
        -background {#d9d9d9} -height 95 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 160 
    vTcl:DefineAlias "$top.lab43" "Labelframe4" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab43
    radiobutton $site_3_0.rad43 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Idle -variable {} 
    vTcl:DefineAlias "$site_3_0.rad43" "Radiobutton1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_3_0.rad44 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Calibration -variable {} 
    vTcl:DefineAlias "$site_3_0.rad44" "Radiobutton2" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_3_0.rad45 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Active -variable {} 
    vTcl:DefineAlias "$site_3_0.rad45" "Radiobutton3" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.rad43 \
        -in $site_3_0 -x 10 -y 20 -width 48 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.rad44 \
        -in $site_3_0 -x 10 -y 40 -width 86 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.rad45 \
        -in $site_3_0 -x 10 -y 60 -width 68 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $top.lab44 \
        -font TkDefaultFont -foreground black -text {Selection Tool} \
        -background {#d9d9d9} -height 115 -width 160 
    vTcl:DefineAlias "$top.lab44" "Labelframe5" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab44
    button $site_3_0.but45 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command Button -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Ball Calibration} 
    vTcl:DefineAlias "$site_3_0.but45" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but46 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Servo Calibration} 
    vTcl:DefineAlias "$site_3_0.but46" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but47 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Ball position} 
    vTcl:DefineAlias "$site_3_0.but47" "Button3" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but45 \
        -in $site_3_0 -x 10 -y 20 -width 141 -relwidth 0 -height 24 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but46 \
        -in $site_3_0 -x 10 -y 50 -width 141 -relwidth 0 -height 24 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 10 -y 80 -width 141 -relwidth 0 -height 24 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab51 \
        -in $top -x 660 -y 360 -width 160 -relwidth 0 -height 155 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 660 -y 520 -width 160 -relwidth 0 -height 155 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 660 -y 280 -width 160 -relwidth 0 -height 75 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab43 \
        -in $top -x 660 -y 180 -width 160 -relwidth 0 -height 95 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 660 -y 60 -width 160 -relwidth 0 -height 115 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

