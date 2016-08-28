function rollDice()
{	
	console.log("entered");
	numDice = document.getElementById("diceInput").value;
	
	var diceRolls = [];
	
	for (var i=0; i<numDice; i++)
	{
		var roll = Math.random();
		
		if (roll >= 0 && roll < (1/6))
		{
			roll = 1;
		}
		else if (roll >= (1/6) && roll < (1/3))
		{
			roll = 2;
		}
		else if (roll >= (1/6) && roll < (1/2))
		{
			roll = 3;
		}
		else if (roll >= (1/2) && roll < (2/3))
		{
			roll = 4;
		}
		else if (roll >= (2/3) && roll < (5/6))
		{
			roll = 5;
		}
		else
		{
			roll = 6;
		}
		diceRolls.push(roll);
		document.getElementById("diceDiv").innerHTML += diceRolls[i] + ' ';
	}
}