from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    BURGER_CONSTRUCTOR_SECTION = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")
    ORDER_FEED_TAB = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    COMPLETED_ORDERS_SECTION = (By.XPATH, "//p[contains(text(),'Готовы:')]")
    BUN_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")
    CONSTRUCTOR_TARGET_ZONE = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    ORDER_SUCCESS_NOTIFICATION = (By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']")
    ORDER_IN_PROGRESS_ITEM = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']//li[1]//*[contains(text(), '{0}')]")