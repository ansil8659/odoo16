odoo.define('point_of_sale.PurchaseLimitPOS', function (require) {
    'use strict';

    const { parse } = require('web.field_utils');
    const PosComponent = require('point_of_sale.PosComponent');
    const { useErrorHandlers } = require('point_of_sale.custom_hooks');
    const NumberBuffer = require('point_of_sale.NumberBuffer');
    const { useListener } = require("@web/core/utils/hooks");
    const Registries = require('point_of_sale.Registries');
    const { isConnectionError } = require('point_of_sale.utils');
    const utils = require('web.utils');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    console.log("qwerty")
//    var rpc = require('web.rpc')

    const PurchaseLimitPOS = (PaymentScreen) =>
    class extends PaymentScreen {

        async validateOrder() {
            const customer = this.currentOrder.get_partner();
            const amount = this.currentOrder.get_total_with_tax();
            const line = this.currentOrder.get_paymentlines();
            console.log("000000000000000", line.name)

            console.log("check+++++++++++++", customer.warn_amount)
            console.log("local#########", amount)
            console.log("---------------------   ", line)
            console.log(line[0].payment_method.name == 'Credit', "0000000000000000")
            console.log("main&&&&&&&&&&&&&&&&&&&&&&", line[0].amount)
            var lenofline = line.length
            console.log('lenofline', lenofline)
            var flag = 0
            var c_id = customer.id
            for(var i=0;i<lenofline;i++){
            console.log("Linr items  ",line[i])

            if (line[i].payment_method.name == 'Credit'){
                if (customer.credit_limit == true){
                    if (customer.credit_amount >= customer.block_amount && customer.block_amount !== 0){

                        this.showPopup('ErrorPopup', {
                                    title: this.env._t('Exceeding Credit Limit'),
                                    body: this.env._t("Sorry the credit allowed will crossed its limit(Credit Limit:" + customer.block_amount + "). Your Current credit is("+ customer.credit_amount +").Please pay using different method or contact manager"),
                                });

                    }
                    else if (customer.credit_amount >= customer.warn_amount && customer.block_amount !== 0){

                        this.showPopup('ErrorPopup', {
                                    title: this.env._t('Exceeding Credit Limit'),
                                    body: this.env._t("Sorry the credit allowed will reached its limit(Credit Limit:" + customer.warn_amount + "). Your Current credit is("+ customer.credit_amount +").Please pay using different method or contact manager"),
                                });
//                        await super.validateOrder()
                          flag = 1

                    }
                    else{
//                        await super.validateOrder()
                          flag = 1
                    }

                }
                else{
                    this.showPopup('ErrorPopup', {
                        title: this.env._t('Credit Account not found'),
                        body: this.env._t("Customer not eligible for credit payment"),
                    });
                }
            }
            else{
//              await super.validateOrder()
                flag = 1
            }
            if (flag == 1){
            await super.validateOrder()
//            rpc.query({
//                model: 'res.partner',
//                method: 'dynamic_update',
//                args: [,c_id, line[i].amount]
//            })

            }
            }

        }

    }
     Registries.Component.extend(PaymentScreen, PurchaseLimitPOS);
      return PaymentScreen;
});
