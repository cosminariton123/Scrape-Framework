def delete_shadow_section_harting(driver_instance, timeout):
        shadow_section = driver_instance.DRIVER.get_element_invisible(xpath = "//*[@id=\"usercentrics-root\"]", timeout = timeout)
        driver_instance.DRIVER.execute_script("""
        var shadow_section = arguments[0];
        shadow_section.parentNode.removeChild(shadow_section);
        """, shadow_section)
        