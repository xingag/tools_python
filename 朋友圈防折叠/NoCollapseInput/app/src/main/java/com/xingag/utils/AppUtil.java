package com.xingag.utils;

import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.util.Log;
import android.view.accessibility.AccessibilityNodeInfo;

import com.xingag.service.PreventService;

import static android.content.Context.CLIPBOARD_SERVICE;


public class AppUtil
{

    /***
     * 获取剪切板上的内容
     * @return
     */
    public static String getClipBoardContent(Context context)
    {
        ClipboardManager cm = (ClipboardManager) context.getSystemService(CLIPBOARD_SERVICE);
        ClipData cd2 = cm.getPrimaryClip();
        String result = "";
        try
        {
            result = cd2.getItemAt(0).getText().toString();
        } catch (Exception e)
        {
            //pass
            Log.d("xag", "产生异常了。。。。");
        }
        return result;
    }

    /***
     * 获取当前页面所有的元素
     * @param node
     */
    public static void getAllNodes(AccessibilityNodeInfo node)
    {
        int count = node.getChildCount();

        if (count == 0)
        {
            PreventService.nodes.add(node);
        } else
        {
            for (int i = 0; i < count; i++)
            {
                getAllNodes(node.getChild(i));
            }
        }
    }
}
