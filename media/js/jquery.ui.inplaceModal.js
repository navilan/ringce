/*
 * jQuery UI Inplace Modal
 * version: 0.1 (2009-01-05)
 * @requires jQuery v1.2.6 or later
 * @requires jQuery UI v1.6 or later

 * Examples and documentation at: http://www.extrazeal.com/jquery/
 *  License: http://www.opensource.org/licenses/mit-license.php
 */
(function($) {
	$.widget("ui.inplaceModal",{
		show: function(){
			widget = this;
			var overlay_html = '';
			$.each(['left', 'top', 'right', 'bottom'], function(){
				var overlay = widget.overlayId(this);
				if($("#" + overlay).length == 0)
					overlay_html += '<div id="' + overlay + '" class="overlay"/>';
			});
			$('body').append(overlay_html);
			$(this.element).attr("hasModal", true);
			this.resizeOverlay(true);
		},
		
		resizeOverlay: function(force){
			if(!force && !$("#" + widget.overlayId("left")).attr("style")) return;
			widget = this;
			container = this.element;
			var pos = $(container).position();
			var width = $(container).width();
			var height = $(container).height();
			var docwidth = $(document).width();
			var docheight = $(document).height();
			$("#" + widget.overlayId("top")).css({
				height: pos.top,
				width: '100%'
			});
			$("#" + widget.overlayId("left")).css({
				top: pos.top,
				height: docheight - pos.top,
				width: pos.left
			});
			$("#" + widget.overlayId("right")).css({
				top: pos.top,
				left: pos.left + width + 20,
				height: docheight - pos.top,
				width: docwidth - pos.left - width - 20
			});
			$("#" + widget.overlayId("bottom")).css({
				top: pos.top + height + 20,
				left:pos.left,
				width: width + 20,
				height: docheight - pos.top - height - 20
			});
		},
		
		hide: function(){
			var widget = this;
			$(this.element).attr("hasModal", false);
			$.each(['left', 'top', 'right', 'bottom'], function(){
				$("#" + widget.overlayId(this)).removeAttr("style");
			});
		},
		
		overlayId: function(side){
			container = this.element;
			var id = '';
			containerId = $(container).attr("id");
			if(containerId)
				id = containerId;
			else
				id = $(container).parent()[0].id;
			 return id + "_overlay_" + side;
		}
	});
	
})(jQuery);
