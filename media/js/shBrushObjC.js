/**
 * Code Syntax Highlighter for Objective-C.
 * Version 0.0.2
 * Copyright (C) 2006 Shin, YoungJin.
 * http://www.jiniya.net/lecture/techbox/test.html
 * 
 * This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General 
 * Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) 
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied 
 * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more 
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to 
 * the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
 */

dp.sh.Brushes.ObjC = function()
{
	var datatypes =
	'char bool BOOL double float int ' +
	'long short id void';

	var keywords = 
	//'@property @selector @interface @end @implementation @synthesize ' +
	'IBAction IBOutlet SEL YES NO readwrite readonly nonatomic nil NULL ' +
	'super self copy ' +
	'break case catch class const copy __finally __exception __try ' +
	'const_cast continue private public protected __declspec ' + 
	'default delete deprecated dllexport dllimport do dynamic_cast ' + 
	'else enum explicit extern if for friend goto inline ' + 
	'mutable naked namespace new noinline noreturn nothrow ' + 
	'register reinterpret_cast return selectany ' + 
	'sizeof static static_cast struct switch template this ' + 
	'thread throw true false try typedef typeid typename union ' + 
	'using uuid virtual volatile whcar_t while';

	this.regexList = [
		{ regex: dp.sh.RegexLib.SingleLineCComments,				css: 'comment' },			// one line comments
		{ regex: dp.sh.RegexLib.MultiLineCComments,					css: 'comment' },			// multiline comments
		{ regex: dp.sh.RegexLib.DoubleQuotedString,					css: 'string' },			// strings
		{ regex: dp.sh.RegexLib.SingleQuotedString,					css: 'string' },			// strings
		{ regex: new RegExp('^ *#.*', 'gm'),						css: 'preprocessor' },
		{ regex: new RegExp(this.GetKeywords(datatypes), 'gm'),		css: 'datatypes' },
		{ regex: new RegExp(this.GetKeywords(keywords), 'gm'),		css: 'keyword' },
		{ regex: new RegExp('\\bNS\\w+\\b', 'g'),					css: 'keyword' },
		{ regex: new RegExp('@\\w+\\b', 'g'),						css: 'keyword' }
		];

	this.CssClass = 'dp-objc';
	this.Style =	'.dp-objc .datatypes { color: #2E8B57; font-weight: bold; }';
}

dp.sh.Brushes.ObjC.prototype	= new dp.sh.Highlighter();
dp.sh.Brushes.ObjC.Aliases	= ['obj-c', 'objc'];