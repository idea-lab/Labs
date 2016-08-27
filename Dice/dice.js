var roll_again = "yes";

while (roll_again==="yes" || roll_again==="y")
{
    var die = prompt("How many dice?");
    for (var i=0, i<die, i++)
    {
        console.log(Math.random(1, 6));
    }
    roll_again = prompt("Roll the dice again?");
}
