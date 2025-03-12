package org.se.lab;

import static java.lang.System.out;

import org.junit.Test;
import org.junit.Ignore;

public class TimeoutTest
{
    @Ignore
    @Test(timeout = 1000)
    public void aMethodWithTimeout()
    {
        out.println("aMethodWithTimeout()");
        while(true);
    }
}
