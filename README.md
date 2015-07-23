**Object Structure**
--------------------

**Main level objects:** Players (Sorted by name) 

A game set is composed of an array of Player Objects. 

 - Property: name  
 - Description: Player unique name identifier

----------

 - Property: lifeStatus
 - Description: Whether player is alive or dead


----------


 - Property: isBlocked
 - Description: If player is blocked, prevents role action.


----------

- Property: isProtected
- Description: If player is protected, prevents kill.

Example
*[ {name: "Fred", lifeStatus: "dead", isBlocked: "yes", isProtected: "no"}, {name: "John", lifeStatus:"alive", isBlocked: "no", isProtected: "no"} ]*


----------


- Property: role
- Description: 2nd level object describing role. 

A role is an object composed of the following properties:

	- Property: priority
	- Description: Order in which night action is performed over others. The greater the number, the greater the priority.

		function role(role, priority, nightAction, dayAction) {
			    this.role = role;
			    this.priority = priority;
			    this.nightAction = nightAction;
			    this.dayAction = dayAction;
		}

		var doctor = new role("Doctor", 10, function(target){for (x in players){if(players[x].name == target){}}})

