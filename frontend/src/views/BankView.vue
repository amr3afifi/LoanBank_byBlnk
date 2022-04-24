<template>
  
<v-container>
      <v-row justify="center">
        
        <v-card width="65%">
              <v-img height="250px" src="https://y26uq11r8xr1zyp0d3inciqv-wpengine.netdna-ssl.com/wp-content/uploads/2019/12/159-1.jpg"></v-img>

              <v-card-title  class="blue--text mt-8"><h2 class="ml-3">Welcome {{ username }}</h2>
              <div style="margin-top:-35px;display:flex; justify-content:flex-end; width:100%; "> <v-btn @click="logOut" color="blue accent-3" dark>Log Out</v-btn></div>
              </v-card-title>
              <br>
              <v-row style="display: flex;align-items: center;justify-content: center;">
                <label>Total in Bank</label>
                <input readonly id="total" style="text-align:center;vertical-align: middle; width:100%;padding: 10px 0; margin: 0;font-size:100px" value="43243" type="text" color="blue accent-3"/>
              </v-row>
              
              <v-row style="display: flex;align-items: center;justify-content: center;">
                <label style="text-align:center;vertical-align: middle;width:50%">Total by Providers</label>
                <label style="text-align:center;vertical-align: middle;width:50%">Total to Customers</label>
              </v-row>
              <v-row  align="center">
                <input readonly id="total_value_prov" style="text-align:center;vertical-align: middle;width:50%;padding: 20px 0 ; margin: 0;font-size:40px" value="131224" type="text" color="blue accent-3"/>
                <input readonly id="total_value_cust" style="text-align:center;vertical-align: middle;width:50%;padding: 20px 0 ; margin: 0;font-size:40px" value="129555" type="text" color="blue accent-3"/>
              </v-row>
              <v-row style="display: flex;align-items: center;justify-content: center;">
                <label style="text-align:center;vertical-align: middle;width:50%">Paid to Providers</label>
                <label style="text-align:center;vertical-align: middle;width:50%">Collected from Customers</label>
              </v-row>
              <v-row  align="center">
                <input readonly id="total_paid_prov" style="text-align:center;vertical-align: middle;width:50%;padding: 20px 0; margin: 0;font-size:40px" value="10000" type="text" color="blue accent-3"/>
                <input readonly id="total_paid_cust" style="text-align:center;vertical-align: middle;width:50%;padding: 20px 0; margin: 0;font-size:40px" value="5000" type="text" color="blue accent-3"/>
              </v-row>
<br><br>

        </v-card>

        <v-card width="65%">
              <v-img height="50px" src="https://y26uq11r8xr1zyp0d3inciqv-wpengine.netdna-ssl.com/wp-content/uploads/2019/12/159-1.jpg"></v-img>

              <form @submit.prevent="createLoanTermCustomer">
                <v-card-text>
                  <div class="font-weight-bold ml-8 mb-2"><h2 align="center" justify="center">Create New Loan Term (Customer)</h2></div><br>

                  <v-row  align="center">
                    <v-text-field id="loanTermName_customer" style=" width:100%;padding: 10px 10px 0 10px; margin: 0px 0;" label="Loan Term Name" name="loanName"  required type="text" color="blue accent-3"/>
                  </v-row>

                  <div>
                      <v-row cols="10" sm="6" md="2">
                        <v-text-field required type="number" id="min_customer" min="0" label="Min" amount class="ml-4"></v-text-field>
                        <v-text-field required type="number" id="max_customer" min="0" label="Max" amount class="ml-4"></v-text-field>
                      </v-row>

                      <v-row cols="10" sm="6" md="2">
                        <v-text-field required type="number" id="duration_customer" min="0" label="Duration" amount class="ml-4"></v-text-field>
                        <v-text-field required type="number" id="interest_customer" min="0" label="Interest" amount class="ml-4"></v-text-field>
                      </v-row>

                      <br><div style="display: flex;align-items: center;justify-content: center;"><v-btn type="submit" color="blue accent-3 ml-5 mr-4" dark >Submit</v-btn></div>
                  </div> <br>

                </v-card-text>
              </form>
        </v-card>


        <v-card width="65%">
          <v-img height="50px" src="https://y26uq11r8xr1zyp0d3inciqv-wpengine.netdna-ssl.com/wp-content/uploads/2019/12/159-1.jpg"></v-img>

          
          <form @submit.prevent="createLoanTermProvider">
              <v-card-text>
                <div class="font-weight-bold ml-8 mb-2"><h2 align="center" justify="center">Create New Loan Term (Provider)</h2>   </div><br>
                
                <v-row  align="center">
                  <v-text-field id="loanTermName_provider" style=" width:100%;padding: 10px 10px 0 10px; margin: 0px 0;" label="Loan Term Name" name="loanName"  required type="text" color="blue accent-3"/>
                </v-row>

                <div>
                    <v-row cols="10" sm="6" md="2">
                      <v-text-field required type="number" id="min_provider" min="0" label="Min" amount class="ml-4"></v-text-field>
                      <v-text-field required type="number" id="max_provider" min="0" label="Max" amount class="ml-4"></v-text-field>
                    </v-row>

                    <v-row cols="10" sm="6" md="2">
                      <v-text-field required type="number" id="duration_provider" min="0" label="Duration" amount class="ml-4"></v-text-field>
                      <v-text-field required type="number" id="interest_provider" min="0" label="Interest" amount class="ml-4"></v-text-field>
                    </v-row>

                    <br><div style="display: flex;align-items: center;justify-content: center;"><v-btn type="submit" color="blue accent-3 ml-5 mr-4" dark >Submit</v-btn></div>
                </div> <br>

              </v-card-text>
          </form>
        </v-card>


        <v-card width="65%">
          <v-img height="50px" src="https://y26uq11r8xr1zyp0d3inciqv-wpengine.netdna-ssl.com/wp-content/uploads/2019/12/159-1.jpg"></v-img>

  
          <v-card-text>
            <div class="font-weight-bold ml-8 mb-2"><h2 align="center" justify="center">Pending Approval Loans (Customer)</h2>   </div>
  
            <v-timeline align-top dense>
              <v-timeline-item v-for="message in pendingLoansCustomer" 
              :key="message.id" small>

                <div>
                  <div class="font-weight-normal">
                      
                    <strong>Name: {{ message.name }} | ID:{{message.id}}</strong>
                  </div>
                  <div>Value= {{ message.value }} $ , Paid= {{ message.paid }} $ , Percentage= {{((message.paid/message.value)*100).toFixed(1)}}%  , Duration= {{ message.duration }} months </div>
                 
                 
                  <div align="right" justify="center"> <v-btn color="green accent-3" dark @click="approveDeclineCustomer(message.id,message.value,true)">Accept</v-btn> <v-btn color="red accent-3" dark @click="approveDeclineCustomer(message.id,message.value,false)">Decline</v-btn></div>    

                </div>
                
              </v-timeline-item>
            </v-timeline>

          </v-card-text>
        </v-card>


        <v-card width="65%">
          <v-img height="50px" src="https://y26uq11r8xr1zyp0d3inciqv-wpengine.netdna-ssl.com/wp-content/uploads/2019/12/159-1.jpg"></v-img>

  
          <v-card-text>
            <div class="font-weight-bold ml-8 mb-2"><h2 align="center" justify="center">Pending Approval Funds (Provider)</h2>   </div>
  
            <v-timeline align-top dense>
              <v-timeline-item v-for="message in pendingLoansProvider" 
              :key="message.id" small>

                <div>
                  <div class="font-weight-normal">
                      
                    <strong>Name: {{ message.name }} | ID:{{message.id}}</strong>
                  </div>
                  <div>Value= {{ message.value }} $ , Paid= {{ message.paid }} $ , Percentage= {{((message.paid/message.value)*100).toFixed(1)}}%  , Duration= {{ message.duration }} months </div>
                 
                 
                  <div align="right" justify="center"> <v-btn color="green accent-3" dark @click="approveDeclineProvider(message.id,true)">Accept</v-btn> <v-btn color="red accent-3" dark @click="approveDeclineProvider(message.id,false)">Decline</v-btn></div>    

                </div>
                
              </v-timeline-item>
            </v-timeline>

          </v-card-text>
        </v-card>


        <v-card width="65%">
          <v-img height="50px" src="https://y26uq11r8xr1zyp0d3inciqv-wpengine.netdna-ssl.com/wp-content/uploads/2019/12/159-1.jpg"></v-img>
  
          <v-card-text>
            <div class="font-weight-bold ml-8 mb-2"><h2 align="center" justify="center">Active Loans (Customer)</h2>   </div>
  
            <v-timeline align-top dense>
              <v-timeline-item v-for="message in activeLoansCustomer" :key="message.id" small>
                
                <div>
                  <div class="font-weight-normal">
                    <strong>Name: {{ message.name }} | ID:{{message.id}}</strong>
                  </div>
                  <div>Value= {{ message.value }} $ , Paid= {{ message.paid }} $ , Percentage= {{((message.paid/message.value)*100).toFixed(1)}}%  </div>
                  <div>Duration= {{ message.duration }} months , Started in & Ends in </div>
                  <br>
                 
                </div>
                
              </v-timeline-item>
            </v-timeline>

          </v-card-text>
        </v-card>



        <v-card width="65%">
          <v-img height="50px" src="https://y26uq11r8xr1zyp0d3inciqv-wpengine.netdna-ssl.com/wp-content/uploads/2019/12/159-1.jpg"></v-img>
  
          <v-card-text>
            <div class="font-weight-bold ml-8 mb-2"><h2 align="center" justify="center">Active Funds (Provider)</h2>   </div>
  
            <v-timeline align-top dense>
              <v-timeline-item v-for="message in activeLoansProvider" :key="message.id" small>
                
                <div>
                  <div class="font-weight-normal">
                    <strong>Name: {{ message.name }} | ID:{{message.id}}</strong>
                  </div>
                  <div>Value= {{ message.value }} $ , Paid= {{ message.paid }} $ , Percentage= {{((message.paid/message.value)*100).toFixed(1)}}% </div>
                  <div>Duration= {{ message.duration }} months , Started in & Ends in </div>

                  <div>
                        <v-row cols="10" sm="1" md="1">  
                          <v-text-field label="Amount" type="number" @change="changePaymentValue" amount class="ml-4"></v-text-field>
                          <v-btn color="blue accent-3 ml-5 mr-4" dark @click="makePayment(message.id)" >Make Payment</v-btn>
                        </v-row> 
                  </div>
                  <br>
                 
                </div>
                
              </v-timeline-item>
            </v-timeline>

          </v-card-text>
        </v-card>
    
      </v-row>
    </v-container>
 
</template>


<script>
const API_URL = 'http://localhost:8000/'
import axios from 'axios'


export default {
    name: 'Bank',

    data () {
    return {

      username: '',
      userID:1,
      paymentValue:0,
      loanTermCustomer:{},
      loanTermProvider:{},

    activeLoansCustomer: [],
    activeLoansProvider: [],
    pendingLoansCustomer: [],
    pendingLoansProvider: [],
    }
  },
  props: {
    source: String
  },
  mounted () {

    
    this.username=this.$store.state.user.username;
    this.userID=this.$store.state.user.id;
    this.getBankStats();
    this.getPendingLoansCustomer();
    this.getActiveLoansCustomer();
    this.getPendingLoansProvider();
    this.getActiveLoansProvider();
    
  },
  methods: {

    logOut()
    {
      sessionStorage.clear()
      this.$store.commit("setAuthentication", false);
      this.$store.commit("setUser", {});
      window.location.reload();
    },
    getBankStats()
    {
       axios({
        method: 'get',
        url: API_URL + 'getBankStats/',  
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         console.log(response.data);
         if(response.data.status=="success")
         {
           document.getElementById('total_value_cust').value=response.data.sumValCust;
           document.getElementById('total_value_prov').value=response.data.sumValProv;
           document.getElementById('total_paid_cust').value=response.data.paidValCust;
           document.getElementById('total_paid_prov').value=response.data.paidValProv;
           document.getElementById('total').value=(response.data.sumValProv+response.data.paidValCust)-(response.data.paidValProv+response.data.sumValCust);
         }

        })
    },

    getPendingLoansCustomer() {
      axios({
        method: 'get',
        url: API_URL + 'getPendingLoan/'+0+'/'+0,
        
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         console.log(response.data);
         this.pendingLoansCustomer=response.data;

        })
    },

    getActiveLoansCustomer() {
  axios({
    method: 'get',
    url: API_URL + 'getActiveLoan/'+0+'/'+1,
    
    auth: {
      username: 'admin',
      password: '12345'
    }
  }).then((response) => {
      console.log(response.data);
      this.activeLoansCustomer=response.data;

    })
},

    getPendingLoansProvider() {
      axios({
        method: 'post',
        url: API_URL + 'getPendingLoan/'+0+'/'+0,
        
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         console.log(response.data);
         this.pendingLoansProvider=response.data;

        })
    },

    getActiveLoansProvider() {
  axios({
    method: 'post',
    url: API_URL + 'getActiveLoan/'+0+'/'+1,
    
    auth: {
      username: 'admin',
      password: '12345'
    }
  }).then((response) => {
      console.log(response.data);
      this.activeLoansProvider=response.data;

    })
},
    approveDeclineCustomer(loanNum,value,status) {
      if(document.getElementById('total').value>=value)
      {
      axios({
        method: 'post',
        url: API_URL + 'approveDeclineLoan/',
        data: {
            loanNum: loanNum,
            status:status
          },
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         console.log(response);
          this.getPendingLoansCustomer();
          this.getActiveLoansCustomer();
          this.getBankStats();
        })
      }
      else
      alert('Bank does not have enough cash to provide this loan')
        

    
},

createLoanTermProvider() {
      var name= document.getElementById('loanTermName_provider').value;
      var minv= document.getElementById('min_provider').value;
      var maxv= document.getElementById('max_provider').value;
      var duration= document.getElementById('duration_provider').value;
      var interest= document.getElementById('interest_provider').value;
if (name && minv && maxv && duration && interest) {

      axios({
        method: 'put',
        url: API_URL + 'createLoanTerm/',
        data: {
            name: name,
            min:minv,
            max:maxv,
            duration:duration,
            interest:interest
          },
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         console.log(response);
        if(response.data.status=="success")
          alert('Loan Term created successfully')
        else
          alert("Error:"+response.data.message)

        })
}
        

    
},

createLoanTermCustomer() {
      var name= document.getElementById('loanTermName_customer').value;
      var minv= document.getElementById('min_customer').value;
      var maxv= document.getElementById('max_customer').value;
      var duration= document.getElementById('duration_customer').value;
      var interest= document.getElementById('interest_customer').value;
if (name && minv && maxv && duration && interest) {

      axios({
        method: 'post',
        url: API_URL + 'createLoanTerm/',
        data: {
            name: name,
            min:minv,
            max:maxv,
            duration:duration,
            interest:interest
          },
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         console.log(response);
        if(response.data.status=="success")
          alert('Loan Term created successfully')
        else
          alert("Error:"+response.data.message)

        })
}
        

    
},
changePaymentValue(e)
{
this.paymentValue=parseInt(e);

},
makePayment(loanNum) {
      if (this.paymentValue && this.paymentValue>0) {
      axios({
        method: 'put',
        url: API_URL + 'makePayment/',
        data: {
            loanNum: loanNum,
            value: this.paymentValue
          },
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         console.log(response);
        if(response.data.message)
          alert(response.data.message)
          
        if(response.data.status=="success")  
          this.getActiveLoansProvider();
          this.getBankStats();
          
        })
      }
      else
      alert('Please enter valid payment value');

    
},
    approveDeclineProvider(loanNum,status) {
      axios({
        method: 'put',
        url: API_URL + 'approveDeclineLoan/',
        data: {
            loanNum: loanNum,
            status:status
          },
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         console.log(response);
          this.getPendingLoansProvider();
          this.getActiveLoansProvider();
          this.getBankStats();
        })
        

    
},

  }
};
</script>
