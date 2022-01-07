[
+++++				set cell0 to 5
[				loop until cell0 is 0
	>+++++			set cell1 to 5
	[			loop until cell1 is 0
		>++++		increase cell2 by 4
		>++++		increase cell3 by 4
	<<-]			decrease cell1 by 1			
	>+++			increase cell2 by 1
	>+			increase cell3 by 1
<<<-]				decrease cell0 by 1				
>>.				print cell2
>...				print cell3 3 times
<++.......			decrease cell2 by 2; print cell2 7 times 
]