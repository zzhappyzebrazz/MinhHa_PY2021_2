var _0x98fd = [".overlapblackbg, .slideLeft", ".wsmenucontent", "menuopen", "addClass", "menuclose", "removeClass", "hasClass", "click", "#navToggle", "mrginleft", "toggleClass", ".wsmenucontainer", "on", "#navToggle,.overlapblackbg", '<span class="wsmenu-click"><i class="wsmenu-arrow fa fa-angle-down"></i></span>', "prepend", ".wsmenu-submenu, .wsmenu-submenu-sub, .wsmenu-submenu-sub-sub", "has", ".wsmenu-list li", ".megamenu", "slow", "slideToggle", ".wsmenu-list", ".wsmenu-mobile", ".wsmenu-submenu",
    "siblings", "wsmenu-rotate", ".wsmenu-arrow", "children", ".wsmenu-submenu-sub", ".wsmenu-submenu-sub-sub", ".wsmenu-click"
];
$(function() {
    var headings = $(_0x98fd[0]);
    var emptyJ = $(_0x98fd[1]);
    /**
     * @return {undefined}
     */
    var backdrop = function() {
        $(headings)[_0x98fd[5]](_0x98fd[4])[_0x98fd[3]](_0x98fd[2]);
    };
    /**
     * @return {undefined}
     */
    var _element = function() {
        $(headings)[_0x98fd[5]](_0x98fd[2])[_0x98fd[3]](_0x98fd[4]);
    };
    $(_0x98fd[8])[_0x98fd[7]](function() {
        if (emptyJ[_0x98fd[6]](_0x98fd[2])) {
            $(_element);
        } else {
            $(backdrop);
        }
    });
    emptyJ[_0x98fd[7]](function() {
        if (emptyJ[_0x98fd[6]](_0x98fd[2])) {
            $(_element);
        }
    });
    $(_0x98fd[13])[_0x98fd[12]](_0x98fd[7], function() {
        $(_0x98fd[11])[_0x98fd[10]](_0x98fd[9]);
    });
    $(_0x98fd[18])[_0x98fd[17]](_0x98fd[16])[_0x98fd[15]](_0x98fd[14]);
    $(_0x98fd[18])[_0x98fd[17]](_0x98fd[19])[_0x98fd[15]](_0x98fd[14]);
    $(_0x98fd[23])[_0x98fd[7]](function() {
        $(_0x98fd[22])[_0x98fd[21]](_0x98fd[20]);
    });
    $(_0x98fd[31])[_0x98fd[7]](function() {
        $(this)[_0x98fd[25]](_0x98fd[24])[_0x98fd[21]](_0x98fd[20]);
        $(this)[_0x98fd[28]](_0x98fd[27])[_0x98fd[10]](_0x98fd[26]);
        $(this)[_0x98fd[25]](_0x98fd[29])[_0x98fd[21]](_0x98fd[20]);
        $(this)[_0x98fd[25]](_0x98fd[30])[_0x98fd[21]](_0x98fd[20]);
        $(this)[_0x98fd[25]](_0x98fd[19])[_0x98fd[21]](_0x98fd[20]);
    });
});