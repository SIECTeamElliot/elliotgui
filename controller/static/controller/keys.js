function Key(id, type, text) {
	this.id = id;
	this.type = type;
	this.text = text;
	this.state = false;

	this.btn = document.createElement("BUTTON");
	this.btn.id = this.id;

	this._bind = function(fct, obj) {
		return function() {
			return fct.apply(obj, arguments);
		};
	};

	this._onMouseDown = function () {
		$('#hidden').load("event?type=" + this.type + "&trig=down");
	};

	this._onMouseUp = function () {
		$('#hidden').load("event?type=" + this.type + "&trig=up");	
	};

	this.onMouseDown = this._bind(this._onMouseDown, this); 
	this.onMouseUp = this._bind(this._onMouseUp, this); 

	this.btn.onmousedown = this.onMouseDown; 
	this.btn.onmouseup = this.onMouseUp; 

	this.btn.appendChild(document.createTextNode(this.text)); 

	keys.appendChild(this.btn); 
}

function TrigKey(type) {
	this.f = function(e) {
		switch(e.which) {
			case 32: 
				$('#stop').trigger(type);
			break;

		    case 37: // left	
				$('#left').trigger(type);
		    break;

		    case 38: // up
				$('#up').trigger(type);
		    break;

		    case 39: // right
				$('#right').trigger(type);
		    break;

		    case 40: // down
				$('#down').trigger(type);
		    break;

		    default: return; // exit this handler for other keys
		}
		e.preventDefault(); // prevent the default action (scroll / move caret)
	}
}

var buttonUp = new Key("up", "up", "\u25b2"); 
var buttonDown = new Key("down", "down", "\u25bc"); 
var buttonLeft = new Key("left", "left", "\u25c0");
var buttonRight = new Key("right", "right", "\u25b6"); 
var buttonStop = new Key("stop", "stop", "\u25cf");

$(document).keydown( (new TrigKey('onmousedown')).f );	
$(document).keyup( (new TrigKey('onmouseup')).f );	