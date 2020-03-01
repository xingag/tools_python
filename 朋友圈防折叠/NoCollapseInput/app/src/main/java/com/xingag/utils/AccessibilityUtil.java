package com.xingag.utils;

import android.app.ActivityManager;
import android.app.AlertDialog;
import android.content.ComponentName;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.provider.Settings;
import android.text.TextUtils;

import com.xingag.preventrubbishapp.R;

import java.util.List;

public class AccessibilityUtil
{
    private Context mContext;
    private String locPackageName;
    private String accessibilityClassAbsolutePath;

    /**
     * 构造方法
     *
     * @param mContext
     * @param accessibilityClassAbsolutePath
     */
    public AccessibilityUtil(Context mContext, String locPackageName,
                             String accessibilityClassAbsolutePath
    )
    {
        this.mContext = mContext;
        this.locPackageName = locPackageName;
        this.accessibilityClassAbsolutePath = accessibilityClassAbsolutePath;
    }


    /**
     * 判断是否有辅助功能权限
     *
     * @return 是否开启服务
     */
    public static boolean isAccessibilitySettingsOn(Context context, String className)
    {
        if (context == null)
        {
            return false;
        }
        ActivityManager activityManager = (ActivityManager) context.getSystemService(Context.ACTIVITY_SERVICE);
        // 获取正在运行的服务列表
        List<ActivityManager.RunningServiceInfo> runningServices =
                activityManager.getRunningServices(300);
        for (int i = 0; i < runningServices.size(); i++)
        {
            ComponentName service = runningServices.get(i).service;
            if (service.getClassName().equals(className))
            {
                return true;
            }
        }
        return false;
    }

    public boolean isAccessibilitySettingsOn()
    {
        boolean isAccessibilityOn = false;
        try
        {
            int accessibilityEnabled = Settings.Secure.getInt(mContext.getContentResolver(), Settings.Secure.ACCESSIBILITY_ENABLED);
            TextUtils.SimpleStringSplitter mStringColonSplitter = new TextUtils.SimpleStringSplitter(':');
            if (accessibilityEnabled == 1)
            {
                String settingValue = Settings.Secure.getString(mContext.getContentResolver(), Settings.Secure.ENABLED_ACCESSIBILITY_SERVICES);
                if (settingValue != null)
                {
                    TextUtils.SimpleStringSplitter splitter = mStringColonSplitter;
                    splitter.setString(settingValue);
                    while (splitter.hasNext())
                    {
                        String accessabilityService = splitter.next();
                        //辅助服务关键路径，格式如"com.corget/com.corget.service.UnAccessibilityService"
                        String service = locPackageName + "/" + accessibilityClassAbsolutePath;
                        if (accessabilityService.equalsIgnoreCase(service))
                        {
                            isAccessibilityOn = true;
                        }
                    }
                }
            }
        } catch (Settings.SettingNotFoundException e)
        {
            e.printStackTrace();
        }
        return isAccessibilityOn;
    }


    public void openSettingDialog()
    {
        AlertDialog.Builder mDialogBuilder = new AlertDialog.Builder(mContext);

        mDialogBuilder.setIcon(R.mipmap.ic_launcher);
        mDialogBuilder.setTitle("警告");
        mDialogBuilder.setMessage("防折叠服务没有开启，请先开启服务");
        mDialogBuilder.setCancelable(false);
        mDialogBuilder.setPositiveButton("Sure",
                new DialogInterface.OnClickListener()
                {
                    @Override
                    public void onClick(DialogInterface dialog, int which)
                    {
                        dialog.dismiss();
                        openSettingPage();
                    }
                });
        mDialogBuilder.setNegativeButton("Cancel",
                new DialogInterface.OnClickListener()
                {
                    @Override
                    public void onClick(DialogInterface dialog, int which)
                    {
                        dialog.dismiss();
                    }
                });
        mDialogBuilder.create().show();
    }

    /***
     * 打开设置界面
     */
    public void openSettingPage()
    {
        Intent startIntent = new Intent(
                Settings.ACTION_ACCESSIBILITY_SETTINGS);
        mContext.startActivity(startIntent);
        mContext.sendBroadcast(new Intent()
                .setAction("com.xingag.setting.dialog"));
    }


}
