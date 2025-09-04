[[Lake/Memory/Shared Memory]] that's only shared until it's tried to be written. On write, it's copied (`fork()`-ed) by OS so that child process will not modify parent process allocated memory.
