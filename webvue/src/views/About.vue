<template>
  <div class="app">
    <!-- 头部 -->
    <div class="header">
      <span class="header_left">
        <i class="el-icon-school" /> 教育部全国高校名单（截止2020-06-30）</span>
      <div class="header_right">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="按高校查询" name="first" />
          <el-tab-pane label="按地区查询" name="second" />
        </el-tabs>
      </div>
    </div>

    <!-- 中部 -->
    <el-container class="container">
      <!-- 导航栏 -->
      <el-aside class="container_left" width="200px">
        <!-- 搜索 -->
        <el-card v-model="flag">
          <el-autocomplete v-model="serchText" style="width:178px;hieght:36px;margin:25px 12px 0 10px" class="inline-input" :fetch-suggestions="querySearch" placeholder="请输入关键词" :trigger-on-focus="false" @click="handleSelect" />
          <el-button type="primary" class="btn" style="width:178px;hieght:33px;margin:10px 10px 0px 10px" @click="handleSelect">查询</el-button>
          <p class="ziti" style="margin:12px 10px 25px 10px">
            <span class="red_dot">*</span>
            请输入关键词并点击查询
          </p>
        </el-card>
      </el-aside>

      <!-- 表格栏 -->
      <el-card class="container_right">
        <el-header><span class="dot">●</span><span style="float:left">全国普通高等学校名单</span></el-header>
        <el-main>
          <el-table :data="school_info" stripe show-overflow-tooltip :cell-style="{ fontSize: '13px', padding: '0' }" style="z-index: 10" :row-style="{ height: '0px' }">
            <el-table-column type="index" label="№" width="40" align="center" />
            <el-table-column prop="school_code" label="学校标识码" width="90" align="center">
              <template #default="{row}">
                {{ row.School_code }}
              </template>
            </el-table-column>
            <el-table-column prop="school_name" label="学校名称" width="200" align="center">
              <template #default="{row}">
                {{ row.School_name }}
              </template>
            </el-table-column>
            <el-table-column prop="school_province" label="所在地区" width="130" align="center">
              <template #default="{row}">
                {{ row.School_zone }}
              </template>
            </el-table-column>
            <el-table-column prop="school_city" label="所在城市" width="90" align="center">
              <template #default="{row}">
                {{ row.School_city }}
              </template>
            </el-table-column>
            <el-table-column prop="school_department" label="主管部门" min-width="90" align="center">
              <template #default="{row}">
                {{ row.School_department }}
              </template>
            </el-table-column>
            <el-table-column prop="school_level" label="办学层次" width="80" align="center">
              <template #default="{row}">
                {{ row.School_level }}
              </template>
            </el-table-column>
            <el-table-column prop="school_type" label="高校类型" align="center">
              <template #default="{row}">
                {{ row.School_type }}
              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-card>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      flag: true,
      school_info: null, // 储存全部学校信息
      serchText: '',
      school_province: [
        { key: '1', value: '北京市' },
        { key: '2', value: '广东省' },
        { key: '3', value: '山东省' },
        { key: '4', value: '江苏省' },
        { key: '5', value: '河南省' },
        { key: '6', value: '上海市' },
        { key: '7', value: '河北省' },
        { key: '8', value: '浙江省' },
        { key: '9', value: '天津市' },
        { key: '10', value: '四川省' },
        { key: '11', value: '陕西省' },
        { key: '12', value: '湖南省' },
        { key: '13', value: '重庆市' },
        { key: '14', value: '吉林省' },
        { key: '15', value: '云南省' },
        { key: '16', value: '福建省' },
        { key: '17', value: '安徽省' },
        { key: '18', value: '海南省' },
        { key: '19', value: '江西省' },
        { key: '20', value: '湖北省' },
        { key: '21', value: '辽宁省' },
        { key: '22', value: '山西省' },
        { key: '23', value: '台湾省' },
        { key: '24', value: '黑龙江' },
        { key: '25', value: '西藏区' },
        { key: '26', value: '青海省' },
        { key: '27', value: '贵州省' },
        { key: '28', value: '甘肃省' },
        { key: '29', value: '宁夏回族自治区' },
        { key: '30', value: '广西壮族自治区' },
        { key: '31', value: '新疆维吾尔自治区' },
        { key: '32', value: '内蒙古自治区' },
        { key: '33', value: '澳门特别行政区' },
        { key: '34', value: '香港特别行政区' }
      ],
      school_type: [
        { key: '1', value: '一流大学' },
        { key: '2', value: '一流学科' },
        { key: '3', value: '985高校' },
        { key: '4', value: '211高校' }
      ],
      submenu: {
        school_type: '',
        school_province: ''
      },
      activeName: 'first',
      school_id: undefined,
      school_code: undefined,
      school_name: undefined,
      school_city: undefined,
      school_department: undefined,
      school_level: undefined,
      activeType: '一流大学',
      school_website: undefined
    }
  },

  methods: {
    handleSelect() {
      console.log(this.serchText)
      axios.get('http://127.0.0.1:8083/school' + '?searchText=' + this.serchText).then(response => {
        this.school_info = response.data.data
      })
    },
    getdata(key) {
      var quest = 'is_firstuniversity=1'
      if (key === 1) {
        quest = 'is_firstuniversity=1'
        this.activeType = '一流大学'
      } else if (key === 2) {
        quest = 'is_firstdiscipline=1'
        this.activeType = '一流学科'
      } else if (key === 3) {
        quest = 'is_985=1'
        this.activeType = '985高校'
      } else if (key === 4) {
        quest = 'is_211=1'
        this.activeType = '211高校'
      }
      axios.get('http://127.0.0.1:8083/school' + '?' + quest).then(response => {
        this.school_info = response.data.data
      })
    },
    handleClick(tab, event) {
      // console.log(tab, event)
      console.log(tab.index)
      if (tab.index === '0') {
        this.first()
      } else {
        this.second()
      }
    },
    first() {
      this.$router.push({
        name: 'About'
      })
    },
    second() {
      this.$router.push({
        name: 'Home'
      })
    }
  }
}
</script>

<style lang='scss'>
// 全局样式
.app {
  width: 1150px;
  margin: auto;
}

// 头部样式
.header {
  position: relative;
  height: 50px;
  background-color: #f2f8fe;
  border-radius: 6px;

  .el-icon-school {
    margin-left: 10px;
  }

  .header_left {
    position: absolute;
    margin-top: 13px;

    .el-icon-school {
      color: #4285f4;
    }
  }

  .header_right {
    float: right;
    width: 200px;
  }
}

// 中部样式
.container {
  margin-top: 15px;
  // height: 500px;

  .container_left {
    .container_left_menu {
      border-right: 0px;

      .submenu {
        background-color: #f8f8f8;
      }
    }
  }

  .container_right {
    margin-left: 15px;
    width: 100%;

    .dot {
      color: #4285f4;
      margin-right: 10px;
      float: left;
    }

    .el-header {
      border-bottom: 2px solid #4285f4;
      color: #333;
      line-height: 60px;
    }
  }
}
.btn {
  display: inline-block;
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
  color: #fff;
  border: none;
  text-align: center;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  outline: none;
  margin: 0;
  padding: 10px 20px;
  font-size: 13px;
  border-radius: 4px;
  font-family: inherit;
  margin: 12px 0;
  width: 100%;
  background-color: #4285f4;
}
.red_dot {
  margin-right: 5px;
  vertical-align: middle;
  color: red;
}
.ziti {
  font-size: 12px;
  color: #999;
}
// element-ui卡片单独样式
.el-card__body {
  padding: 0;
}
.el-main {
  padding: 0;
}
.el-table .cell {
  padding: 2px;
}
.cell {
  padding: 2px;
}
.el-table--border td:first-child .cell,
.el-table--border th:first-child .cell {
  padding-left: 2px;
}
</style>
