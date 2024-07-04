with GNAT.Lock_Files;
with Ada.Text_IO;
procedure main is

begin

GNAT.Lock_Files.Lock_File( "/tmp/mylockfile.lock", Wait => 15.0, Retries => 2 );
Ada.Text_IO.Put_Line("Ready");

GNAT.Lock_Files.Unlock_File( "/tmp/mylockfile.lock" );
end main;