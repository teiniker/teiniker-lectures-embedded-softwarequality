# Decompiling Assembly Code with ChatGPT

## ChatGPT Prompt

```
Decompile the given assembly code into C source code: 
                    ********************************************
                    *                 FUNCTION                 *
                    ********************************************
                    undefined main()
         undefined    AL:1      <RETURN>
         undefined4   Stack[-0x local_c                     XREF[2]: 001011aa(W), 
                                                                     001011b1(R)  
         undefined8   Stack[-0x local_18                    XREF[2]: 001011ad(W), 
                                                                     001011d0(R)  
                    main                              XREF[4]: Entry Point(*), 
                                                               _start:00101084(*), 
                                                               00102088, 00102160(*)  
   001011a2 55         PUSH    RBP
   001011a3 48 89 e5   MOV     RBP,RSP
   001011a6 48 83      SUB     RSP,0x10
            ec 10
   001011aa 89 7d fc   MOV     dword ptr [RBP + local_c],EDI
   001011ad 48 89      MOV     qword ptr [RBP + local_18],RSI
            75 f0
   001011b1 83 7d      CMP     dword ptr [RBP + local_c],0x2
            fc 02
   001011b5 74 19      JZ      LAB_001011d0
   001011b7 48 8d      LEA     RAX,[s_Usage:_secret_<password>_  = "Usage: secret <pass
            05 69 
            0e 00 00
   001011be 48 89 c7   MOV     RDI=>s_Usage:_secret_<password>_  = "Usage: secret <pass
   001011c1 e8 6a      CALL    <EXTERNAL>::puts                  int puts(char * __s)
            fe ff ff
   001011c6 bf 00      MOV     EDI,0x0
            00 00 00
   001011cb e8 80      CALL    <EXTERNAL>::exit                  void exit(int __status)
            fe ff ff
                    -- Flow Override: CALL_RETURN (CALL_TERMIN
                    LAB_001011d0                      XREF[1]: 001011b5(j)  
   001011d0 48 8b      MOV     RAX,qword ptr [RBP + local_18]
            45 f0
   001011d4 48 83      ADD     RAX,0x8
            c0 08
   001011d8 48 8b 00   MOV     RAX,qword ptr [RAX]
   001011db 48 89 c7   MOV     RDI,RAX
   001011de e8 8b      CALL    is_correct_password               undefined is_correct_p
            ff ff ff
   001011e3 85 c0      TEST    EAX,EAX
   001011e5 74 0f      JZ      LAB_001011f6
   001011e7 e8 6d      CALL    get_secret                        undefined get_secret()
            ff ff ff
   001011ec 48 89 c7   MOV     RDI,RAX
   001011ef e8 3c      CALL    <EXTERNAL>::puts                  int puts(char * __s)
            fe ff ff
   001011f4 eb 0f      JMP     LAB_00101205
                    LAB_001011f6                      XREF[1]: 001011e5(j)  
   001011f6 48 8d      LEA     RAX,[s_Invalid_password!_00102040]= "Invalid password!"
            05 43 
            0e 00 00
   001011fd 48 89 c7   MOV     RDI=>s_Invalid_password!_0010204  = "Invalid password!"
   00101200 e8 2b      CALL    <EXTERNAL>::puts                  int puts(char * __s)
            fe ff ff
                    LAB_00101205                      XREF[1]: 001011f4(j)  
   00101205 b8 00      MOV     EAX,0x0
            00 00 00
   0010120a c9         LEAVE
   0010120b c3         RET
```

## ChatGPT 

Below is a plausible C reconstruction of the given assembly snippet. I've added comments to show how each assembly instruction maps to the C code. Note that decompiled code is never a perfect 1:1 representation of the original source—but this gets you close.

```c
#include <stdio.h>
#include <stdlib.h>

// These are references to functions used by the assembly code:
extern int  is_correct_password(const char *password);
extern char *get_secret(void);

int main(int argc, char *argv[])
{
    // Compare argc to 2
    if (argc != 2)
    {
        puts("Usage: secret <password>");
        exit(0);
    }

    // If password is correct
    if (is_correct_password(argv[1]))
    {
        char *secret = get_secret();
        puts(secret);
    }
    else
    {
        puts("Invalid password!");
    }

    return 0;
}
```

### How This Maps to the Assembly

1. **Function prologue:**
   ```assembly
   001011a2 55              PUSH RBP
   001011a3 48 89 e5        MOV  RBP, RSP
   001011a6 48 83 ec 10     SUB  RSP, 0x10
   ```
   - Standard function entry: save old base pointer, set up new stack frame, reserve stack space.

2. **Save `argc` and `argv`:**
   ```assembly
   001011aa 89 7d fc        MOV  [RBP + local_c], EDI   // argc
   001011ad 48 89 75 f0     MOV  [RBP + local_18], RSI  // argv
   ```

3. **Check `argc`:**
   ```assembly
   001011b1 83 7d fc 02     CMP  [RBP + local_c], 2
   001011b5 74 19           JZ   LAB_001011d0
   ```
   - If `argc` == 2, jump to the password check (label `LAB_001011d0`). Otherwise, print usage and exit.

4. **Print usage and exit:**
   ```assembly
   001011b7 48 8d 05 69 ...  LEA  RAX, [rip + "Usage: secret <password>"]
   001011be 48 89 c7         MOV  RDI, RAX               // puts argument
   001011c1 e8 6a fe ff ff   CALL <EXTERNAL>::puts
   001011c6 bf 00 00 00 00   MOV  EDI, 0
   001011cb e8 80 fe ff ff   CALL <EXTERNAL>::exit
   ```

5. **`LAB_001011d0`: Access `argv[1]` and check password:**
   ```assembly
   001011d0 48 8b 45 f0      MOV  RAX, [RBP + local_18]  // RAX = argv
   001011d4 48 83 c0 08      ADD  RAX, 8                 // RAX = &argv[1]
   001011d8 48 8b 00         MOV  RAX, [RAX]             // RAX = argv[1]
   001011db 48 89 c7         MOV  RDI, RAX
   001011de e8 8b ff ff ff   CALL is_correct_password
   001011e3 85 c0            TEST EAX, EAX               // if return == 0 ...
   001011e5 74 0f            JZ   LAB_001011f6           // ... jump if password is wrong
   ```

6. **If password is correct:**
   ```assembly
   001011e7 e8 6d ff ff ff   CALL get_secret
   001011ec 48 89 c7         MOV  RDI, RAX               // address of secret string
   001011ef e8 3c fe ff ff   CALL <EXTERNAL>::puts
   001011f4 eb 0f            JMP  LAB_00101205           // jump past "invalid" message
   ```

7. **If password is incorrect:**
   ```assembly
   001011f6 48 8d 05 43 ...  LEA  RAX, [rip + "Invalid password!"]
   001011fd 48 89 c7         MOV  RDI, RAX               // puts argument
   00101200 e8 2b fe ff ff   CALL <EXTERNAL>::puts
   ```

8. **End of function:**
   ```assembly
   00101205 b8 00 00 00 00   MOV  EAX, 0
   0010120a c9               LEAVE
   0010120b c3               RET
   ```

So, in plain C, the logic is:

1. If `argc != 2`, print usage and exit.  
2. If `argc == 2`, call `is_correct_password(argv[1])`.  
    - If it returns non-zero (true), retrieve the secret via `get_secret()` and print it.  
    - Otherwise, print `"Invalid password!"`.  
3. Finally, return 0.

*Egon Teiniker, 2025, GPL v3.0*