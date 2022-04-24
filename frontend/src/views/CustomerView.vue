<template>
  
<v-container>
      <v-row justify="center">

        <v-card width="65%">
            <v-img height="250px" src="https://www.beepquest.com/wp-content/uploads/2021/06/Acompan%CC%83amiento-constante.png"></v-img>

            <v-card-title  class="blue--text mt-8"><h2 class="ml-3">Welcome {{ username }}</h2>
          <div style="margin-top:-35px;display:flex; justify-content:flex-end; width:100%; "> <v-btn @click="logOut" color="blue accent-3" dark>Log Out</v-btn></div>
          </v-card-title>


            <form @submit.prevent="requestLoan">
            <v-card-text>
              <div class="font-weight-bold ml-8 mb-2"><h2 align="center" justify="center">Request New Loan</h2>   </div>
              <v-row  align="center">
                <v-text-field id="loanName" style=" width:100%;padding: 10px 10px 0 10px; margin: 0px 0;" label="Loan Name" name="loanName"  required type="text" color="blue accent-3"/>
                <v-col v-if="checkloanterm">
                 <v-select id='loan' :rules="[(v) => !!v || 'Loan Term is required']" required :items="loans" :menu-props="{ top: false, offsetY: true }" label="Loan Term" @change="changeLoanDetails"></v-select>
                </v-col>
              </v-row>

              <div><p>Loan Details</p>
              <input type="text" style=" width:100%;padding: 10px; margin: 10px 0; border-bottom: thin solid grey;" id='loanDetails' readonly>
              </div>

              <div><br>
                  <v-row cols="10" sm="6" md="3">
                    <v-text-field required type="number" id="loanValue" min="0" label="Amount" amount class="ml-4"></v-text-field>
                    <v-btn type="submit" color="blue accent-3 ml-5 mr-4" dark >Submit</v-btn>
                  </v-row>
              </div> <br>

            </v-card-text>
            </form>
        </v-card>



        <v-card width="65%">
          <v-img height="50px" src="https://www.beepquest.com/wp-content/uploads/2021/06/Acompan%CC%83amiento-constante.png"></v-img>

          <v-card-text>
            <div class="font-weight-bold ml-8 mb-2"><h2 align="center" justify="center">Pending Approval Loans</h2></div>

            <v-timeline align-top dense>
              <v-timeline-item v-for="message in pendingLoans" :key="message.id" small>

                <div>
                  <div class="font-weight-normal"><strong>Name: {{ message.name }} | ID:{{message.id}}</strong></div>
                  <div>Value= {{ message.value }} $ , Paid= {{ message.paid }} $ , Percentage= {{((message.paid/message.value)*100).toFixed(1)}}%  , Duration= {{ message.duration }} months </div>
                  <div align="right" justify="center"> <v-btn color="red accent-3" dark @click="cancelLoan(message.id)">Cancel</v-btn></div>  
                </div>
                
              </v-timeline-item>
            </v-timeline>

          </v-card-text>
        </v-card>

        <v-card width="65%">
          <v-img height="50px" src="https://www.beepquest.com/wp-content/uploads/2021/06/Acompan%CC%83amiento-constante.png"></v-img>
              <v-card-text>
                <div class="font-weight-bold ml-8 mb-2"><h2 align="center" justify="center">Active Loans</h2> </div>
      
                <v-timeline align-top dense>
                  <v-timeline-item v-for="message in activeLoans" :key="message.id" small>
                    
                    <div>
                      <div class="font-weight-normal"><strong>Name: {{ message.name }} | ID:{{message.id}}</strong> </div>
                      <div>Value= {{ message.value }} $ , Paid= {{ message.paid }} $ , Percentage= {{((message.paid/message.value)*100).toFixed(1)}}% </div>
                      <div>Duration= {{ message.duration }} months , Started in & Ends in </div><br>

                      <div>
                        <v-row cols="10" sm="1" md="1">  
                          <v-text-field label="Amount" type="number" @change="changePaymentValue" amount class="ml-4"></v-text-field>
                          <v-btn color="blue accent-3 ml-5 mr-4" dark @click="makePayment(message.id)" >Make Payment</v-btn>
                        </v-row> 
                      </div>
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
    name: 'Customer',

    data () {
    return {
      username: '',
      loanName: '',
      userID:1,
      loanValue:1,
      paymentValue:0,
      selectedTerm:'',
      selectedTermId:0,
      checkloanterm:false,

      loans: [],
      loanTerms:  [],
      activeLoans: [],
      pendingLoans: [],
    }
  },
  props: {
    source: String
  },
  mounted () {

    
    this.username=this.$store.state.user.username;
    this.userID=this.$store.state.user.id;
    this.getLoanTerms();
    this.getPendingLoans();
    this.getActiveLoans();
    
  },
  methods: {

getLoanTerms() {
      axios({
        method: 'get',
        url: API_URL + 'getLoanTerm/',
        
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         this.loanTerms=response.data;

         for (let i = 0; i < this.loanTerms.length; i++) {
          this.loans[i]=this.loanTerms[i]['name'];
        }
        this.checkloanterm=true;

        })
    },

getPendingLoans() {
      axios({
        method: 'get',
        url: API_URL + 'getPendingLoan/'+this.userID+'/'+0,
        
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {

        console.log("pending");
        console.log(response.data);
        this.pendingLoans=response.data;


        })
    },

getActiveLoans() {
  axios({
    method: 'get',
    url: API_URL + 'getActiveLoan/'+this.userID+'/'+1,
    
    auth: {
      username: 'admin',
      password: '12345'
    }
  }).then((response) => {
      console.log("active");
      console.log(response.data);
      this.activeLoans=response.data;


    })
},

changeLoanDetails(e) {
  this.selectedTerm=e;
      for (let i = 0; i < this.loanTerms.length; i++) {
          if (e==this.loanTerms[i]['name'])
            {document.getElementById('loanDetails').value="min= "+this.loanTerms[i]['min'] +"$, max= "+this.loanTerms[i]['max']+"$, duration= "+this.loanTerms[i]['duration']+"months, interest= "+this.loanTerms[i]['interest']+"%";
          this.selectedTermId=this.loanTerms[i]['id'];}

        }
        this.checkloanterm=true;
    },

requestLoan() {

      this.loanValue = document.getElementById('loanValue').value;
      this.loanName = document.getElementById('loanName').value;
if (this.loanName && this.loanValue) {
      axios({
        method: 'post',
        url: API_URL + 'requestLoan/',
        data: {
            name: this.loanName ,
            value: this.loanValue,
            user_id: this.userID,
            term_id: this.selectedTermId
          },
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         console.log(response);
         this.getPendingLoans();
        })
    }},

logOut()
    {
      sessionStorage.clear()
      this.$store.commit("setAuthentication", false);
      this.$store.commit("setUser", {});
      window.location.reload();
    },

makePayment(loanNum) {
      if (this.paymentValue && this.paymentValue>0) {
      axios({
        method: 'post',
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
          this.getActiveLoans();
          
        })
      }
      else
      alert('Please enter valid payment value');

    
},

changePaymentValue(e)
{
this.paymentValue=parseInt(e);

},

cancelLoan(loanNum) {
      axios({
        method: 'delete',
        url: API_URL + 'cancelLoan/',
        data: {
            loanNum: loanNum
          },
        auth: {
          username: 'admin',
          password: '12345'
        }
      }).then((response) => {
         console.log(response);
          this.getPendingLoans();
        })
        

    
}
  }
};
</script>
