if((navigator.userAgent.toLowerCase().indexOf('msie 6') != -1) &&
 (navigator.userAgent.toLowerCase().indexOf('msie 7') == -1)){
    if( !document.referrer ||
        (document.referrer.indexOf(document.location.hostname) === -1 &&
        document.referrer.indexOf("itsobsolete") === -1)){
        document.location.href =
         "http://ie6.itsobsolete.com?title=Ringce&url=" +
         escape(document.location.href);    
    }
}