package com.xingag.service;

import android.accessibilityservice.AccessibilityService;
import android.annotation.TargetApi;
import android.content.Intent;
import android.os.Build;
import android.text.TextUtils;
import android.util.Log;
import android.view.accessibility.AccessibilityEvent;
import android.view.accessibility.AccessibilityNodeInfo;
import android.widget.Toast;

import com.xingag.utils.AppUtil;

import java.util.ArrayList;
import java.util.List;

public class PreventService extends BaseService
{
    //所有的节点
    public static List<AccessibilityNodeInfo> nodes = new ArrayList<>();

    private static final String CLASS_NAME_SNS_UPLOAD = "com.tencent.mm.plugin.sns.ui.SnsUploadUI";

    /**
     * 连接服务成功后回调该方法
     */
    @Override
    protected void onServiceConnected()
    {
        super.onServiceConnected();
        //缓存中获取数据
        Toast.makeText(PreventService.this, "连接服务成功",
                Toast.LENGTH_SHORT).show();

        stopSelf();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId)
    {
        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public void onAccessibilityEvent(AccessibilityEvent event)
    {
        //如果是朋友圈发布界面
        String className = event.getClassName().toString();

        Log.d("xag", "className:" + className);

        if (TextUtils.equals(CLASS_NAME_SNS_UPLOAD, className))
        {
            Log.e("xag", "朋友圈发布界面");

            //获取剪切板的内容
            String content = AppUtil.getClipBoardContent(getApplicationContext());

            if (!TextUtils.isEmpty(content))
            {
                Log.d("xag", "剪切板内容是:" + content);
                inputContent(event, content);
            } else
            {
                Log.d("xag", "剪切板内容为空");
            }
        }

    }


    /***
     * 回复消息
     * @param event
     */
    private void inputContent(AccessibilityEvent event, String content)
    {
        //获取输入框元素
        //方式一
//        AccessibilityNodeInfo chat_edit = findViewByID("com.tencent.mm:id/d41");

        //方式二
        nodes.clear();
        AppUtil.getAllNodes(getRootInActiveWindow());
        AccessibilityNodeInfo chat_edit = findNodeInfoByClassName("android.widget.EditText");

        //把文本输入到输入框内
        inputText(chat_edit, content);
    }


    /***
     * 通过类名查找元素
     * @param className
     * @return
     */
    public AccessibilityNodeInfo findNodeInfoByClassName(String className)
    {
        for (int i = 0; i < nodes.size(); i++)
        {
            //当前节点元素及classname
            AccessibilityNodeInfo currentNode = nodes.get(i);
            String tagClassName = currentNode.getClassName().toString();

            Log.d("xag", "tagClassName:" + tagClassName);
            if (TextUtils.equals(tagClassName, className))
            {
                Log.d("xag", "元素找到了");
                return currentNode;
            }
        }
        Log.d("xag", "元素没找到");
        return null;
    }


    @Override
    public void onInterrupt()
    {
        Log.d("xag", "无障碍服务被打断");
    }


    @Override
    public void onDestroy()
    {
        super.onDestroy();
        Log.d("xag", "无障碍服务销毁");
    }
}
