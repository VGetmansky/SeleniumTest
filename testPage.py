class testPageValues:
    _base_page_title ='Смартфоны - купить смартфон: цены, отзывы, характеристики, продажа смартфонов в каталоге' \
                      ' интернет-магазина СИТИЛИНК '

    _min_value_name = "input-min"
    _max_Value_name = "input-max"

    _cell_price_xpath = '//span[@class="ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price "]'
    _cell_filter_tag = '//div[@class="FilterTags__tag js--FilterTags__tag"]'

    def set_base_page_title(self):
        return self._base_page_title

    def set_min_value_name(self):
        return self._min_value_name

    def set_max_value_name(self):
        return self._max_Value_name

    def set_cell_price_xpath(self):
        return self._cell_price_xpath

    def set_cell_filter_tag(self):
        return self._cell_filter_tag
