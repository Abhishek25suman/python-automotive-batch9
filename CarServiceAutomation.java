package Demo;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.net.URI;
import java.net.URL;
import java.time.Duration;
import java.text.SimpleDateFormat;
import java.util.Date;
import io.appium.java_client.AppiumBy;


import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.io.FileHandler;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;

public class CarServiceAutomation {

    static AndroidDriver driver;
    static FileWriter report;

    public static void main(String[] args) throws Exception {

        report = new FileWriter("TestReport.html");
        report.write("<html><body><h2>Car Service Automation Report</h2>");

        UiAutomator2Options options = new UiAutomator2Options();
        options.setPlatformName("Android");
        options.setAutomationName("UiAutomator2");
        options.setDeviceName("E6LN5T7HJBBEVWPZ");
        options.setAppPackage("br.com.ctncardoso.ctncar");
        options.setAppActivity("br.com.ctncardoso.ctncar.StartActivity");
        options.setNoReset(true);
        options.setNewCommandTimeout(Duration.ofSeconds(60));

        URL url = URI.create("http://127.0.0.1:4723").toURL();
        driver = new AndroidDriver(url, options);

        Thread.sleep(8000);

        System.out.println("================= App Started Successfully =================");
        Thread.sleep(3000);

        try {

            addReminder();
            editReminder();
            deleteReminder();

            report.write("<p style='color:green'>All Test Cases PASSED</p>");

        } catch (Exception e) {

            takeScreenshot("Failure");
            report.write("<p style='color:red'>Test Case FAILED</p>");
            e.printStackTrace();
        }

        report.write("</body></html>");
        report.close();
        driver.terminateApp("br.com.ctncardoso.ctncar");
        System.out.println("================= App Working Properly =================");

        Thread.sleep(2000);
        driver.quit();
    }

    // ================= ADD REMINDER =================
    public static void addReminder() throws Exception {

        System.out.println("Executing Add Reminder");

        // Click + icon
        driver.findElement(By.id("br.com.ctncardoso.ctncar:id/novo")).click();
        Thread.sleep(2000);

        // Click Reminder
        driver.findElement(By.xpath("//android.widget.TextView[@text=\"Reminder\"]")).click();
        Thread.sleep(2000);

        // Click Service
        driver.findElement(By.xpath("//android.widget.TextView[@resource-id=\"br.com.ctncardoso.ctncar:id/fs_texto2\" and @text=\"Service\"]")).click();
        Thread.sleep(2000);

        // Click Type of service
        driver.findElement(By.xpath("//android.widget.TextView[@resource-id=\"br.com.ctncardoso.ctncar:id/fb_valor\" and @text=\"Type of service\"]")).click();
        Thread.sleep(2000);

        // Scroll and select Oil change
        driver.findElement(
        	    AppiumBy.androidUIAutomator(
        	        "new UiScrollable(new UiSelector().scrollable(true))"
        	        + ".scrollIntoView(new UiSelector().text(\"Oil Change\"))"
        	    )
        	).click();
        Thread.sleep(2000);

        // Enter 5000 in Odometer
        driver.findElement(By.id("br.com.ctncardoso.ctncar:id/et_odometro"))
                .sendKeys("5000");
        Thread.sleep(2000);

        // Enable Date checkbox
        driver.findElement(By.id("br.com.ctncardoso.ctncar:id/cb_periodo"))
                .click();
        Thread.sleep(2000);

        // Open Date Picker
        driver.findElement(By.xpath("//android.widget.TextView[@resource-id=\"br.com.ctncardoso.ctncar:id/fb_label\" and @text=\"Date\"]")).click();
        Thread.sleep(2000);

        // Select 25
        driver.findElement(By.xpath("//android.view.View[@content-desc=\"25 February 2026\"]")).click();
        Thread.sleep(1000);

        driver.findElement(By.id("android:id/button1")).click(); // OK
        Thread.sleep(2000);

        // Enter Notes
        driver.findElement(By.id("br.com.ctncardoso.ctncar:id/et_observacao"))
                .sendKeys("Change engine oil");
        Thread.sleep(2000);

        // Save
        driver.findElement(By.xpath("//android.widget.Button[@content-desc=\"Save\"]")).click();
        Thread.sleep(3000);

        System.out.println("Add Reminder Passed");
        Thread.sleep(2000);

    }

    // ================= EDIT REMINDER =================
    public static void editReminder() throws Exception {

        System.out.println("Executing Edit Reminder");

        // Open Reminder section at bottom
        driver.findElement(By.xpath("//android.widget.FrameLayout[@content-desc=\"Reminders\"]")).click();
        Thread.sleep(2000);

        // Open Oil change data
        driver.findElement(By.xpath("//android.widget.LinearLayout[@resource-id=\"br.com.ctncardoso.ctncar:id/fundo\"]")).click();
        Thread.sleep(2000);

        // Edit Odometer 5000 -> 6000
        driver.findElement(By.id("br.com.ctncardoso.ctncar:id/et_odometro")).clear();
        driver.findElement(By.id("br.com.ctncardoso.ctncar:id/et_odometro")).sendKeys("6000");
        Thread.sleep(2000);

        // Change Date
        driver.findElement(By.xpath("//android.widget.TextView[@resource-id=\"br.com.ctncardoso.ctncar:id/fb_label\" and @text=\"Date\"]")).click();
        Thread.sleep(2000);

        driver.findElement(By.xpath("//android.widget.ImageButton[@content-desc=\"Next month\"]")).click();
        driver.findElement(By.xpath("//android.view.View[@content-desc=\"10 March 2026\"]")).click();
        Thread.sleep(1000);

        driver.findElement(By.id("android:id/button1")).click(); // OK
        Thread.sleep(2000);

        // Save
        driver.findElement(By.xpath("//android.widget.Button[@content-desc=\"Save\"]")).click();
        Thread.sleep(3000);

        System.out.println("Edit Reminder Passed");
        Thread.sleep(2000);

    }

    // ================= DELETE REMINDER =================
    public static void deleteReminder() throws Exception {

        System.out.println("Executing Delete Reminder");
        
        Thread.sleep(3000);
        
        // Open Oil change reminder
        driver.findElement(By.xpath("//android.widget.LinearLayout[@resource-id=\"br.com.ctncardoso.ctncar:id/fundo\"]")).click();
        Thread.sleep(2000);

        // Click Delete icon
        driver.findElement(By.xpath("//android.widget.Button[@content-desc=\"Delete\"]")).click();
        Thread.sleep(2000);

        // Confirm delete in popup
        driver.findElement(By.id("br.com.ctncardoso.ctncar:id/BTN_Sim")).click();
        Thread.sleep(3000);

        System.out.println("Delete Reminder Passed");
        Thread.sleep(2000);
        
    }

    // ================= SCREENSHOT =================
    public static void takeScreenshot(String name) throws IOException {

        File src = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
        String timestamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
        File dest = new File("Screenshot_" + name + "_" + timestamp + ".png");
        FileHandler.copy(src, dest);

        System.out.println("Screenshot Captured");
    }
}
