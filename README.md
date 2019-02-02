
作者：andy
运行平台：windows 7
浏览器: firefox
python版本:3.7
功能说明：
    学习python WEB自动化拨测。模块逐步完善中....
    boce模块主要检查页面最后的元素是否加载完成。
    banliyewu模块从配置文件中获取手机号和密码，自动登陆并打开业务办理页面。
    dnsqry模块用于检测静态域名是否使用CDN边缘节点。因为尚未接入CDN，故判断本地hosts文件。
    每个模块的变量定义都可以通过profile模块读取。
    
备注：模块的配置文件格式示例
<?xml version="1.0" encoding="utf-8"?>
<property>
    <yewubanli>
        <phone>150XXXXXXXX</phone>
        <passwd>111111</passwd>
    </yewubanli>
	<boce>
		<timeout></timeout>
		<count>20</count>
	</boce>
</property>



