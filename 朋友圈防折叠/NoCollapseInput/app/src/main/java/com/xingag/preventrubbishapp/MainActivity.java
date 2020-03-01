package com.xingag.preventrubbishapp;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.TextView;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import com.xingag.utils.AccessibilityUtil;

public class MainActivity extends AppCompatActivity implements View.OnClickListener
{

    //包名和服务名称
    private static final String PACKAGE_NAME = "com.xingag.preventrubbishapp";
    private static final String SERVICE_NAME = "com.xingag.service.PreventService";

    private AccessibilityUtil accessibilityUtil = null;

    //状态
    private TextView status_tv = null;

    private Button open_service_btn = null;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        status_tv = findViewById(R.id.status_tv);
        open_service_btn = findViewById(R.id.open_service_btn);
        open_service_btn.setOnClickListener(this);

        accessibilityUtil = new AccessibilityUtil(MainActivity.this,
                PACKAGE_NAME, SERVICE_NAME);

        //设置标题
        ActionBar actionBar = getSupportActionBar();
        if (actionBar != null)
        {
            actionBar.setTitle("不折叠服务");
        }

        //判断状态，如果没有开启，就跳到设置界面
        openAccessibilityMet();
    }

    public void openAccessibilityMet()
    {
        //服务状态
        boolean status = AccessibilityUtil.isAccessibilitySettingsOn(this, SERVICE_NAME);
        if (!status)
        {
            accessibilityUtil.openSettingDialog();
        }
    }


    @Override
    protected void onResume()
    {
        super.onResume();
        //判断服务状态
        boolean status = AccessibilityUtil.isAccessibilitySettingsOn(this, SERVICE_NAME);
        status_tv.setText(status ? "开启" : "关闭");
    }

    @Override
    public void onClick(View view)
    {
        if (view.getId() == R.id.open_service_btn)
        {
            accessibilityUtil.openSettingPage();
        }
    }
}

