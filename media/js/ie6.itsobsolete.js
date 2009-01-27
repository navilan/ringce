if((navigator.userAgent.toLowerCase().indexOf('msie 6') != -1) &&
 (navigator.userAgent.toLowerCase().indexOf('msie 7') == -1)){
     function beginsWith(full, part){
         if (full.length < part.length) return false;
         else
             return full.substring(0, part.length) === part;
    }
    if( !document.referrer ||
        (!beginsWith(document.referrer, document.location.hostname) &&
        !beginsWith(document.referrer, "http://ie6.itsobsolete.com"))){
        document.location.href =
         "http://ie6.itsobsolete.com?title=Ringce&url=" +
         escape(document.location.href);    
    }
}