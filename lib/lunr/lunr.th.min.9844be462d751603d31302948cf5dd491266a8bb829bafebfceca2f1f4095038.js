/*!
 * Lunr languages, `Thai` language
 * https://github.com/MihaiValentin/lunr-languages
 *
 * Copyright 2017, Keerati Thiwanruk
 * http://www.mozilla.org/MPL/
 *//*!
 * based on
 * Snowball JavaScript Library v0.3
 * http://code.google.com/p/urim/
 * http://snowball.tartarus.org/
 *
 * Copyright 2010, Oleg Mazko
 * http://www.mozilla.org/MPL/
 */(function(e,t){typeof define=="function"&&define.amd?define(t):typeof exports=="object"?module.exports=t():t()(e.lunr)})(this,function(){return function(e){if("undefined"==typeof e)throw new Error("Lunr is not present. Please include / require Lunr before this script.");if("undefined"==typeof e.stemmerSupport)throw new Error("Lunr stemmer support is not present. Please include / require Lunr stemmer support before this script.");var t,n=e.version[0]=="2";e.th=function(){this.pipeline.reset(),this.pipeline.add(e.th.trimmer),n?this.tokenizer=e.th.tokenizer:(e.tokenizer&&(e.tokenizer=e.th.tokenizer),this.tokenizerFn&&(this.tokenizerFn=e.th.tokenizer))},e.th.wordCharacters="[฀-๿]",e.th.trimmer=e.trimmerSupport.generateTrimmer(e.th.wordCharacters),e.Pipeline.registerFunction(e.th.trimmer,"trimmer-th"),t=e.wordcut,t.init(),e.th.tokenizer=function(s){if(!arguments.length||s==null||s==null)return[];if(Array.isArray(s))return s.map(function(t){return n?new e.Token(t):t});var o=s.toString().replace(/^\s+/,"");return t.cut(o).split("|")}}})