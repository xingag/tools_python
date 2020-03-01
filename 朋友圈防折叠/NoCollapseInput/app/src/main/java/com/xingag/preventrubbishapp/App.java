package com.xingag.preventrubbishapp;

import android.app.Application;
import android.content.Context;

public class App extends Application
{
    private static App instance = null;

    public static int phone_type =  0;

    public static App getInstance()
    {
        return instance;
    }

    @Override
    public void onCreate()
    {
        super.onCreate();
        instance = this;
        phone_type = BuildConfig.phone_type;
    }
}
