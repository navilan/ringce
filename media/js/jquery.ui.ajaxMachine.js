/*
 * jQuery UI Inplace Modal
 * version: 0.1 (2009-01-05)
 * @requires jQuery v1.2.6 or later
 * @requires jQuery UI v1.6 or later

 * Examples and documentation at: http://www.extrazeal.com/jquery/
 *  License: http://www.opensource.org/licenses/mit-license.php
 */
(function($) {
	
$.fn.renameAttr = function(name, new_name){
	val = $(this).attr(name);
	$(this).removeAttr(name);
	$(this).attr(new_name, val);
};

$.widget("ui.ajaxMachine",{

	_init: function(){
		this.options.plugins = this.options.plugins || {};
		if(this.options.startStateName)
			this.bindState(this.options.startStateName);
	},

	bindState: function(stateName){
		var state = this.options.states[stateName];
		var widget = this;
		$.each(state.actions, function(){
			this.bind(widget);
		});
	}
});

$.ajaxAction = function(name, nextState, prototype){
	if(!prototype) prototype = $.ajaxActionDefault;
	return $.extend({}, $.ajaxActionDefault, prototype, {name: name, nextState: nextState});
};

$.submitAjaxAction =  function(name, nextState, prototype){
	return $.ajaxAction(name, nextState, $.extend({},$.submitAjaxActionDefault, prototype));
};

$.addAjaxAction =  function(name, nextState, prototype){
	return $.ajaxAction(name, nextState, $.extend({},$.addAjaxActionDefault, prototype));
};

$.deleteAjaxAction =  function(name, nextState, prototype){
	return $.ajaxAction(name, nextState, $.extend({},$.deleteAjaxActionDefault, prototype));
};

$.ajaxActionDefault = {
	_prefix: function(widget){
		return widget.options.prefix(widget.element);
	},
	_hook: function(functionName, widget){
		if(!this[functionName](widget)) return false;
		var action = this;
		var result = true;
		$.each(widget.options.plugins, function(){
			if(!$.isFunction(this[functionName])) result = true;
			else if(!this[functionName](widget, action)) result = false;
			return result;
		});
		return result;
	},
	actionButton: function(widget){
		return $(this._prefix(widget) + "_" + this.name + "_action");
	},
	bind: function(widget){
		if(!this._hook("beforeBind", widget)) return;
		var actionButton = this.actionButton(widget);
		if(!actionButton.length) return;
		actionButton.renameAttr("href", "action");
		var action = this;
		actionButton.unbind('click').bind('click', function(){
			action.act(widget);
		});	
		if(!this._hook("afterBind", widget)) return;
	},
	act: function(widget){
		var action = this;
		if(!this._hook("before", widget)) return;
		this.sendRequest(widget, function(responseText,statusText){
			if(action.processResponse(widget, responseText, statusText)){
				if(action._hook("after", widget) && action.nextState)
					widget.bindState(action.nextState);
			}
		});
	},
	sendRequest: function(widget, responder){
		$.ajax({
			url: this.actionButton(widget).attr("action"),
			success: responder
		});
	},
	processResponse: function(widget, responseText, statusText){
		$(widget.element).html(responseText);
		return true;
	},
	before: function(widget){
		return true;
	},
	after: function(widget){
		return true;
	},
	beforeBind: function(widget){
		return true;
	},
	afterBind: function(widget){
		return true;
	},
	nextState: null
};

$.submitAjaxActionDefault = $.extend({}, $.ajaxActionDefault, {
	actionForm: function(widget){
		return $(this._prefix(widget) + "_" + this.name + "_form");
	},
	afterBind: function(widget){
		var action = this;
		var actionForm = this.actionForm(widget);
		if(!actionForm.length) return;
		actionForm.removeAttr("action");
		actionForm.unbind('submit').bind('submit', function(eventObject){
			if(eventObject.target == this) action.act(widget);
			return false;
		});
	},
	actWithoutAjax: function(widget){
		this.actionForm(widget).unbind('submit');
		this.actionForm(widget).attr("action", this.actionButton(widget).attr("action"));
		this.actionForm(widget).submit();
	},
	sendRequest: function(widget, responder){
		this.actionForm(widget).ajaxSubmit({
			url:$(this.actionButton(widget)).attr("action"), success:responder});
	}
});

$.addAjaxActionDefault = $.extend({}, $.submitAjaxActionDefault, {
	processResponse: function(widget, responseText, statusText){
		$(this._prefix(widget) + "_container").append("<li>" + responseText + "</li>");
		return true;
	}
});

$.deleteAjaxActionDefault = $.extend({}, $.ajaxActionDefault, {
	processResponse: function(widget, responseText, statusText){
		var list_item = $(this.actionButton(widget)).parent();
		while(list_item.length && list_item[0] != widget.element && list_item[0].tagName != "LI"){
			list_item = list_item.parent();
		}
		if(list_item[0].tagName == "LI") $(list_item[0]).remove();
		return true;
	}
});

})(jQuery);
