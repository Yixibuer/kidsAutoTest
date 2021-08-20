from playwright import sync_playwright


def run(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")

    # Fill input[name="wd"]
    page.fill("input[name=\"wd\"]", "测自动化")

    # Press Enter
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=怎么测自动化&fenlei=256&rsv_pq=f793186d0000041f&rsv_t=a9b1QkEB6a2w9oszcDgmAC4L41sIy4R3Cp5ST6wAW3cm5LHUYvryn0V4a6Q&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=2&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=%E6%80%8E%E4%B9%88%E6%B5%8B%E8%87%AA%E5%8A%A8%E5%8C%96&rsp=5&inputT=7417&rsv_sug4=10743"):
    with page.expect_navigation():
        page.press("input[name=\"wd\"]", "Enter")

    # Click input[type="submit"]
    page.click("input[type=\"submit\"]")
    # assert page.url() == "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=怎么测自动化&fenlei=256&oq=%E6%80%8E%E4%B9%88%E6%B5%8B%E8%87%AA%E5%8A%A8%E5%8C%96&rsv_pq=abb8e94800006e1f&rsv_t=49f1Z9lNA2fVYlkQJyr9eXCz5dOLeKdLhFvKsl/EiD3hyXaGOVapKSXW5As&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&prefixsug=%E6%80%8E%E4%B9%88%E6%B5%8B%E8%87%AA%E5%8A%A8%E5%8C%96&rsp=5"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)