Examples of [[Write Skew]]:
- **meeting room booking system** - two users may try to book the same room at the same time (room is free); ^booking
- **double-spending** - two transactions check that there's enough money and both spend so that balance becomes negative;
- **chess multiplayer** - two players may try to put the figures on the same position (cell is empty);
- **user registration** (unique email) - both transactions check that username doesn't exist and both try to insert a new user;

there should always be **at least one doctor** for every slot. Both doctors request sick leave at the same time for the same slot. **Queries check** that there are two doctors for this slot and **both go off**. As a result, **no doctor is left**.