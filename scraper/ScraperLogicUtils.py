def delete_shadow_section_harting(driver_instance):
        shadow_section = driver_instance.DRIVER.find_element_by_xpath("//*[@id=\"usercentrics-root\"]")
        driver_instance.DRIVER.execute_script("""
        var shadow_section = arguments[0];
        shadow_section.parentNode.removeChild(shadow_section);
        """, shadow_section)
        