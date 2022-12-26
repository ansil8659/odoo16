/** @odoo-module **/

var AbstractAction = require('web.AbstractAction');
var core = require('web.core');
var QWeb = core.qweb;
var rpc = require('web.rpc');
var ajax = require('web.ajax');
var outgoing;
var incoming;
var picking_type;
var internal_transfer;
var location_info;
var average_cost;
var date_filter;
var InventoryDashBoard = AbstractAction.extend({
   template: 'InventoryDashBoard',
    events: {
                        'change. #date_filter': 'fetch_data',
    },
init: function(parent, context) {
       this._super(parent, context);
       this.dashboards_templates = ['DashboardProject'];
       this.today_sale = [];
   },
       willStart: function() {
       var self = this;
       return this._super().then(function() {
           return self.fetch_data();
       });
   },
   start: function() {
           var self = this;
           this.set("title", 'Dashboard');
           return this._super().then(function() {
               self.render_dashboards();
           });
       },
       render_dashboards: function(){
       var self = this;
       _.each(this.dashboards_templates, function(template) {
               self.$('.o_pj_dashboard').append(QWeb.render(template, {widget: self}));
           });
   },
fetch_data: function() {
       var self = this;
       date_filter = $("select[name ='date_filter']").val();
       console.log("dfghjkl", date_filter)
       var def1 =  this._rpc({
               model: 'project.project',
               method: 'get_tiles_data',
               args: [date_filter]
   }).then(function(result)
    {
      self.out = result['out']
      self.incmg = result['incmg']
      self.pick_type = result['pick_type']
      self.internal = result['internal']
      self.loc_stock_info = result['loc_stock_info']
      self.avg_cost = result['avg_cost']
       outgoing = result['out'],
       incoming = result['incmg'],
       picking_type = result['pick_type'],
       internal_transfer = result['internal'],
       location_info = result['loc_stock_info'],
       average_cost = result['avg_cost'],




google.charts.load('current', { 'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
//    outgoing
        var line_div = outgoing;
        console.log(line_div)
        var line = line_div.split(/[:,]/);
        console.log(line)
        var array_dt = line.filter((x,i) => (i%2!==0));
        var array_s = line.filter((x,i) => (i%2===0));
        var dataRows = [['', '']];
        for (var i = 0; i < array_s.length; i++) {
          dataRows.push([array_s[i], parseFloat(array_dt[i])]);
        }
        var line_data = google.visualization.arrayToDataTable(dataRows);
        var outgng_label = {
            title: 'Outgoing',
        };
        var cpu_chart = new google.visualization.ColumnChart(document.getElementById('myChart'));
        cpu_chart.draw(line_data,outgng_label);

//        SECOND
        var line_divs = incoming;
        console.log(line_divs)
        var lines = line_divs.split(/[:,]/);
        console.log(lines)
        var array_dts = lines.filter((x,i) => (i%2!==0));
        var array_ss = lines.filter((x,i) => (i%2===0));
        var dataRowss = [['', '']];
        for (var i = 0; i < array_ss.length; i++) {
          dataRowss.push([array_ss[i], parseFloat(array_dts[i])]);
        }
        var line_datas = google.visualization.arrayToDataTable(dataRowss);
        var incmg_label = {
            title: 'Incoming',
        };
        var cpu_charts = new google.visualization.BarChart(document.getElementById('myChartin'));
        cpu_charts.draw(line_datas,incmg_label);

//        picking type group
        var pick_t = picking_type;
        console.log(pick_t)
        var pick_lines = pick_t.split(/[:,]/);
        console.log(pick_lines)
        var pick_array_dts = pick_lines.filter((x,i) => (i%2!==0));
        var pick_array_ss = pick_lines.filter((x,i) => (i%2===0));
        var pick_dataRowss = [['', '']];
        for (var i = 0; i < pick_array_ss.length; i++) {
          pick_dataRowss.push([pick_array_ss[i], parseFloat(pick_array_dts[i])]);
        }
        var pick_line_datas = google.visualization.arrayToDataTable(pick_dataRowss);
        var hole = {
            title: 'Picking Types',
            pieHole: 0.5,
        };
        var pick_cpu_charts = new google.visualization.PieChart(document.getElementById('myChartcount'));
        pick_cpu_charts.draw(pick_line_datas,hole);


//       internal transfer
        var internal_t = internal_transfer;
        console.log(internal_t)
        var internal_lines = internal_t.split(/[:,]/);
        console.log(internal_lines)
        var internal_array_dts = internal_lines.filter((x,i) => (i%2!==0));
        var internal_array_ss = internal_lines.filter((x,i) => (i%2===0));
        var internal_dataRowss = [['', '']];
        for (var i = 0; i < internal_array_ss.length; i++) {
          internal_dataRowss.push([internal_array_ss[i], parseFloat(internal_array_dts[i])]);
        }
        var internal_line_datas = google.visualization.arrayToDataTable(internal_dataRowss);
        var intrnl = {
            title: 'Internal Transfer',
        };
        var internal_cpu_charts = new google.visualization.ColumnChart(document.getElementById('myChartinternal'));
        internal_cpu_charts.draw(internal_line_datas,intrnl);


//       location stock info
        var stock_info = location_info;
        console.log(stock_info)
        var stock_info_lines = stock_info.split(/[:,]/);
        console.log(stock_info_lines)
        var stock_info_array_dts = stock_info_lines.filter((x,i) => (i%2!==0));
        var stock_info_array_ss = stock_info_lines.filter((x,i) => (i%2===0));
        var stock_info_dataRowss = [['', '']];
        for (var i = 0; i < stock_info_array_ss.length; i++) {
          stock_info_dataRowss.push([stock_info_array_ss[i], parseFloat(stock_info_array_dts[i])]);
        }
        var stock_info_line_datas = google.visualization.arrayToDataTable(stock_info_dataRowss);
        var option = {
            title: 'Location',
            pieHole: 0.5,
        };
        var stock_info_cpu_charts = new google.visualization.PieChart(document.getElementById('myChartlocstock'));
        stock_info_cpu_charts.draw(stock_info_line_datas,option);


//       product average cost
//        var avg_cost = l;
//        console.log(avg_cost)
//        var avg_cost_lines = avg_cost.split(/[:,]/);
//        console.log(avg_cost_lines)
//        var avg_cost_array_dts = avg_cost_lines.filter((x,i) => (i%2!==0));
//        var avg_cost_array_ss = avg_cost_lines.filter((x,i) => (i%2===0));
//        var avg_cost_dataRowss = [['', '']];
//        for (var i = 0; i < avg_cost_array_ss.length; i++) {
//          avg_cost_dataRowss.push([avg_cost_array_ss[i], parseFloat(avg_cost_array_dts[i])]);
//        }
//        var avg_cost_line_datas = google.visualization.arrayToDataTable(avg_cost_dataRowss);
////        var option = {
////            title: 'Average Cost',
////            pieHole: 0.5,
////        };
//        var avg_cost_cpu_charts = new google.visualization.BarChart(document.getElementById('myChartavgcost'));
//        avg_cost_cpu_charts.draw(avg_cost_line_datas);



  }
   });
       return $.when(def1);
   },
})
core.action_registry.add('inventory_dashboard_tags', InventoryDashBoard);
return InventoryDashBoard;
//})