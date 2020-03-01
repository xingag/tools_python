package com.xingag.service;

import android.accessibilityservice.AccessibilityService;
import android.accessibilityservice.AccessibilityServiceInfo;
import android.annotation.SuppressLint;
import android.annotation.TargetApi;
import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.os.Build;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.accessibility.AccessibilityEvent;
import android.view.accessibility.AccessibilityManager;
import android.view.accessibility.AccessibilityNodeInfo;


import java.util.List;

/***
 * 无障碍服务的基类
 */


public class BaseService extends AccessibilityService
{

    @SuppressLint("StaticFieldLeak")
    private static BaseService mInstance = null;


    public static BaseService getInstance()
    {
        if (mInstance == null)
        {
            mInstance = new BaseService();
        }
        return mInstance;
    }


    @Override
    public void onAccessibilityEvent(AccessibilityEvent event)
    {

    }

    @Override
    public void onInterrupt()
    {

    }


    /**
     * 模拟输入
     *
     * @param nodeInfo nodeInfo
     * @param text     text
     */
    public void inputText(AccessibilityNodeInfo nodeInfo, String text)
    {
        ClipboardManager clipboard = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);

        Log.d("xag", "字符个数为:" + text.length());
        for (int i = 0; i < text.length(); i++)
        {
            String temp = text.substring(0, i + 1);
            Log.e("xag", "输入一次,输入内容是：" + temp);

            //输入内容
            Bundle arguments = new Bundle();
            arguments.putCharSequence(AccessibilityNodeInfo.ACTION_ARGUMENT_SET_TEXT_CHARSEQUENCE, temp);
            nodeInfo.performAction(AccessibilityNodeInfo.ACTION_SET_TEXT, arguments);

            //下面可以控制输入的速度，这里设置间隔为0.1s
            try
            {
                Thread.sleep(100);
            } catch (InterruptedException e)
            {
                e.printStackTrace();
            }
        }
    }


}
