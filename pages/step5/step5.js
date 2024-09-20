// pages/step5/step5.js
Page({

    /**
     * 页面的初始数据
     */

    goto_step4: function(){
        wx.navigateTo({
          url: '/pages/step4/step4', 
          success: function() { }, 
          fail: function() { }, 
          complete: function() { } 
        })
    },
    goto_step6: function(){
        wx.navigateTo({
          url: '/pages/step6/step6', 
          success: function() { }, 
          fail: function() { }, 
          complete: function() { } 
        })
    },
    data: {

    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad(options) {

    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady() {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow() {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide() {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload() {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh() {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom() {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage() {

    }
})