from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

class TestAutoReactor:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        
    def test_login(self, test_url):
        """Test login លើ website តេស្ត"""
        try:
            self.driver.get(test_url)
            print("✅ បើក website តេស្តដោយជោគជ័យ!")
            
            # សាកល្បងរក input fields
            try:
                # រកមើលទាំងអស់ possible input fields
                inputs = self.driver.find_elements(By.TAG_NAME, "input")
                print(f"🔍 រកឃើញ {len(inputs)} input fields")
                
                for i, input_field in enumerate(inputs):
                    input_type = input_field.get_attribute("type")
                    print(f"Input {i+1}: type={input_type}")
                    
            except Exception as e:
                print(f"⚠️ រកអត់ឃើញ input fields: {e}")
            
            return True
            
        except Exception as e:
            print(f"❌ កំហុសក្នុងការបើក website: {e}")
            return False
    
    def test_react_to_elements(self):
        """Test reactions លើ elements ផ្សេងៗ"""
        try:
            # សាកល្បងចុច buttons ផ្សេងៗ
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            print(f"🔘 រកឃើញ {len(buttons)} buttons")
            
            for i, button in enumerate(buttons[:3]):  # សាកល្បងត្រឹម 3 buttonsសិន 
                try:
                    button_text = button.text or button.get_attribute("innerHTML")
                    print(f"Button {i+1}: {button_text[:50]}...")
                    
                    # សាកល្បងចុចឲ button
                    button.click()
                    print(f"✅ ចុច​បាន {i+1} ដោយជោគជ័យ!")
                    time.sleep(1)
                    
                except Exception as e:
                    print(f"⚠️ មិនអាចចុច button​ បាន {i+1}: {e}")
            
            return True
            
        except Exception as e:
            print(f"❌ កំហុសក្នុងការធ្វើ reactions: {e}")
            return False
    
    def take_screenshot(self, filename="test_result.png"):
        """ថត screenshot នៃលទ្ធផល test"""
        try:
            self.driver.save_screenshot(filename)
            print(f"📸 ថត screenshot ទុកជា {filename}")
        except Exception as e:
            print(f"❌ មិនអាចថត screenshot: {e}")
    
    def close(self):
        """បិទ browser"""
        self.driver.quit()

# TEST SCRIPT - សាក
if __name__ == "__main__":
    bot = TestAutoReactor()
    
    try:
        #  សាកលើ website តេស្ត
        test_websites = [
            "https://httpbin.org/forms/post",  # Website តេស្ត
            "https://example.com",             # Website តេស្តសាមញ្ញ
            "http://localhost:8000"           # Local website (បើមាន)
        ]
        
        for website in test_websites:
            print(f"\n🎌 កំពុង test លើ: {website}")
            print("=" * 50)
            
            success = bot.test_login(website)
            
            if success:
                # រង់ចាំ website load
                time.sleep(3)
                
                # សាកល្បង interactions
                bot.test_react_to_elements()
                
                # ថត screenshot
                bot.take_screenshot(f"test_{website.split('//')[1]}.png")
                
                print(f"✅ បានធ្វើ test លើ {website} ដោយជោគជ័យ!")
            else:
                print(f"❌ មិនអាច test លើ {website}")
            
            time.sleep(2)
            
    except Exception as e:
        print(f"❌ កំហុសក្នុង test script: {e}")
    
    finally:
        bot.close()