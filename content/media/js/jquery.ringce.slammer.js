/*
 * jSlammer
 * Copyright © Lakshmi Vyasarajan, Ringce.com
 * version: 0.1a (2009-11-17 20:28)
 * @requires jQuery v1.3.2 or later

 * Examples and documentation at: http://onlayout.com
 * Dual licensed under the MIT and GPL licenses:
 *   http://www.opensource.org/licenses/mit-license.php
 *   http://www.gnu.org/licenses/gpl.html
 */
(function($) {

   $.slammer = function(element, spec) {

      var plugin = this;
      plugin.$element = $(element);
      plugin.element = element;
      plugin.$element.data("slammer", plugin);
      plugin.init = function(){
          plugin.spec = $.extend({}, spec);
          plugin.spec.layers =  $.extend({}, spec.layers);
          var html = "<div id='layout-canvas-wrapper' style='position:relative'></div>";
          plugin.$element.wrapInner(html);
          plugin.$wrapper = $("#layout-canvas-wrapper");
          html = "<canvas id='layout-canvas' style='z-index:-1;position:absolute;left:0;top:0' width=";
          html += plugin.$element.width();
          html += " height=" + plugin.$element.height();
          html += "></canvas>";
          plugin.$wrapper.prepend(html);
          plugin.canvas = $("#layout-canvas")[0];
      };

      plugin.drawLayer = function(context, layer){
          context.save();
          context.fillStyle = layer.backgroundColor;
          context.globalAlpha = layer.opacity;
          context.globalCompositeOperation = layer.compositeOperation;
          context.fillRect(layer.rect.left, layer.rect.top, layer.rect.width, layer.rect.height);
          context.beginPath();
          context.rect(layer.rect.left, layer.rect.top, layer.rect.width, layer.rect.height);
          context.clip();
          var overlays = $.extend([], layer.overlays);
          jQuery.each(overlays, function(i, overlay){
             plugin.drawOverlay(context, layer, overlay);
          });
          context.restore();
      };

      plugin.drawOverlay = function(context, layer, overlay){
          var radians = overlay.orientation * Math.PI / 180;
          var rect = layer.rect;
          context.save();
          context.translate(rect.left + rect.width - 1, rect.top + rect.height - 1);
          context.rotate(Math.PI);
          context.translate(-rect.left, -rect.top);
          context.globalCompositeOperation = overlay.compositeOperation;
          context.globalAlpha = layer.opacity * overlay.opacity;
          rect = plugin.boundingRectForAngle(radians, layer.rect);
          context.translate(rect.left + rect.width / 2, rect.top + rect.height / 2);
          context.rotate(radians);
          context.translate(-(rect.left + rect.width / 2), -(rect.top + rect.height / 2));
          if (overlay.type == "golden-section"){
              plugin.drawGoldenSection(context, rect, overlay);
          }  else if (overlay.type == "uniform"){
              plugin.drawUniform(context, rect, overlay);
          }   else if (overlay.type == "harmonious-section"){
              plugin.drawHarmoniousSection(context, rect, overlay);
          }
          context.restore();
      };

      plugin.drawGoldenSection = function(context, rect, overlay){
          var bigSection = rect.width / 1.618;
          var smallSection = rect.width - bigSection;
          if(!overlay.bidirectional){
              context.fillStyle = overlay.sectionColor;
              context.fillRect(rect.left, rect.top, bigSection, rect.height);
              context.fillStyle = overlay.alternateColor;
              context.fillRect(rect.left +  bigSection, rect.top, smallSection, rect.height);
          } else {
              var gutter = bigSection - smallSection;
              context.fillStyle = overlay.sectionColor;
              context.fillRect(rect.left, rect.top, smallSection, rect.height);
              context.fillStyle = overlay.alternateColor;
              context.fillRect(rect.left +  smallSection, rect.top, gutter, rect.height);
              context.fillStyle = overlay.sectionColor;
              context.fillRect(rect.left + bigSection, rect.top, smallSection, rect.height);
          }

      };

       plugin.drawHarmoniousSection = function(context, rect, overlay){
            var sectionSize = rect.width / overlay.numberOfSections;
            for (var i = 1; i <= overlay.numberOfSections; i++){
                context.fillStyle =  i % 2 == 1 ? overlay.alternateColor : overlay.sectionColor;
                context.fillRect(rect.left + sectionSize * (i - 1), rect.top, sectionSize, rect.height);
            };
        };

      plugin.drawUniform = function(context, rect, overlay){
          for (var section = 0; section <= rect.width; section += overlay.sectionSize + overlay.gutterSize){
              context.fillStyle = overlay.alternateColor;
              context.fillRect(section + rect.left, rect.top, overlay.gutterSize, rect.height);
              context.fillStyle = overlay.sectionColor;
              context.fillRect(section + rect.left + overlay.gutterSize, rect.top, overlay.sectionSize, rect.height);
          };
      };

      plugin.boundingRectForAngle = function(radians, rect){
        var result = jQuery.extend(true, {}, rect);
        var sineTheta = Math.sin(radians);
        var cosTheta = Math.cos(radians);
        result.width = Math.abs(rect.width * cosTheta) + Math.abs(rect.height * sineTheta);
        result.height = Math.abs(rect.width  * sineTheta) + Math.abs(rect.height * cosTheta);
        result.left -= ((result.width - rect.width) / 2);
        result.top -= ((result.height - rect.height) / 2);
        return result;
      };

      plugin.showAll = function(){
          var context = plugin.canvas.getContext("2d");
          jQuery.each(plugin.spec.layers, function(i, layer){
          plugin.drawLayer(context, layer);
        });
      };

      plugin.hideAll = function(){
        var context = plugin.canvas.getContext("2d");
        context.clearRect(0, 0, plugin.$element.width(), plugin.$element.height());
      };

      plugin.showLayer = function(layerName){
           var matches = $.grep(plugin.spec.layers, function(layer, index){
              layer.name == layerName;

           });
           if (!matches.length) return;
           var layer = matches[0];
           var context = plugin.canvas.getContext("2d");
           plugin.drawLayer(context, layer);
      };

      plugin.init();
      return this;
   };


   $.fn.slammer = function(options){
       if(typeof(options) == "object"){
          (new $.slammer(this[0], options));
       } else if(typeof(options) == "string"){
           var slammer = $(this).data("slammer");
           if(!slammer) return;
           if(options == "showAll"){
               slammer.showAll();
           } else if (options =="hideAll") {
               slammer.hideAll();
           } else {
               slammer.showLayer(options);
           }
       }
   };

 })(jQuery);