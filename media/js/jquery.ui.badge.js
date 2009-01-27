/*
 * jQuery UI Badge
 * version: 0.1 (2009-01-08)
 * @requires jQuery v1.2.6 or later
 * @requires jQuery UI v1.6 or later

 * Examples and documentation at: http://www.ringce.com/code/jquery/
 * Dual licensed under the MIT and GPL licenses:
 *   http://www.opensource.org/licenses/mit-license.php
 *   http://www.gnu.org/licenses/gpl.html
 *
 */

(function($) {

	$.widget("ui.badge",{

		_init: function(){
			var widget = this;
			$(this.element).each( function(){
				if(!$("#" + widget._identifier(this)).length){
					var badge_html = 
						"<div style='position:relative;float:left'>" +
						"<div id='" + widget._identifier(this) + 
						"'/></div>";
					$(this).prepend(badge_html);
				}
			});
			this.show();
		},
		
		_identifier:function(element){
			return element.id + "-ui-widget-badge";
		},
		
		toggle: function(){
			widget = this;
			$(this.element).each(function(){
				$("#" + widget._identifier(this)).toggle();
			});
		},
		
		show: function(opts){
			$.extend(this.options,opts);
			var widget = this;
			$(this.element).each(function(){
				$("#" + widget._identifier(this)).removeAttr("class");
				$("#" + widget._identifier(this)).addClass(widget.options.cssClass);
				$("#" + widget._identifier(this)).show().css({
					position: 'absolute',
					left: widget.options.offset.left,
					top: widget.options.offset.top
				});
				
			});
		},
	
		hide: function(){
			widget = this;
			$(this.element).each(function(){
				$("#" + widget._identifier(this)).hide();
			});
		},
		
		remove: function(){
			$("#" + widget._identifier(this)).parent().remove();
			this.destroy();
		}
	});
	
	$.extend($.ui.badge, {
		defaults: {
			cssClass: "ui-widget-badge",
			offset: {left:0, top:0}
		}
	});

})(jQuery);
