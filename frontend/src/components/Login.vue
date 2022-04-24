

<template>
  
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="6">
            <v-card class="elevation-12">
              <v-window v-model="step">


                <v-window-item :value="1">
                  <v-row>

                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">
                        <h1 class="text-center display-2 blue--text text--accent-3">Blnk!</h1>
                        <h3 class="text-center">Login</h3>
                        <br>
                        <form @submit.prevent="signIn">
                          <v-text-field
                           id="signIn_username"
                            label="Username"
                            name="username"
                            required
                            type="text"
                            color="blue accent-3"
                          />

                          <v-text-field
                            id="signIn_password"
                            label="Password" 
                            required 
                            name="password"
                            type="password"
                            color="blue accent-3"
                           
                          />
                          <div class="text-center mt-3">
                          <v-btn type="submit" color="blue accent-3" dark >SIGN IN</v-btn>
                          </div>

                        </form>
                      </v-card-text>
                      
                        <br>
                    </v-col>

                     <v-col cols="12" md="4" class="blue accent-3">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">Register</h1><br>
                        <h5 class="text-center">Still don't have an account?</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn outlined dark @click="step++">SIGN UP</v-btn>
                      </div>
                    </v-col>

                    
                  </v-row>
                </v-window-item>



                <v-window-item :value="2">
                  <v-row class="fill-height">

                    <v-col cols="12" md="4" class="blue accent-3">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">Login</h1><br>
                        <h5 class="text-center">Have an account already?</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn outlined dark @click="step--">Sign in</v-btn>
                      </div>
                    </v-col>

                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">
                        <h1 class="text-center display-2 blue--text text--accent-3">Blnk!</h1>
                        <h3 class="text-center">Sign Up</h3>
                       
                        <form @submit.prevent="signUp">
                            <v-row align="center">
                              <v-col cols="12">
                                <label>User Type</label>
                                <select style="padding: 10px; margin: 10px 0; border-bottom: thin solid grey;" 
                                  id="signUp_type"
                             
                                  label="User Type"
                                  required
                                  name="userType"
                                >
                                <option value="customer">Customer</option>
                                <option value="provider">Provider</option>
                                <option value="bank">Bank</option>
                                </select>
                              </v-col>
                            </v-row>
                            <v-text-field
                            id="signUp_username"
                              label="Username"
                              required
                              name="username"
                              type="text"
                              color="blue accent-3"
                            />

                            <v-text-field
                              id="signUp_password"
                              required
                              label="Password"
                              name="password"
                              type="password"
                              color="blue accent-3"
                            />
                            <br>
                            <div class="text-center mt-n5">
                        <v-btn type="submit" color="blue accent-3" dark>SIGN UP</v-btn>
                      </div>
                        </form>
                      </v-card-text>
                      
                      
                    </v-col>

                  </v-row>
                </v-window-item>
              </v-window>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
 
</template>


<script>
const API_URL = 'http://localhost:8000/'
import axios from 'axios'


export default {
    name: 'Login',

  
    data: () => ({
    step: 1,
    username: '',
    password: '',
    userType: null,
  }),





  props: {
    source: String
  },
  methods: {

    clear () {
      this.username = ''
      this.password = ''
      this.userType = ''
    },



    signIn() {
      console.log('hi')
      this.username = document.getElementById('signIn_username').value;
      this.password = document.getElementById('signIn_password').value;
      if (this.username && this.password) {
        axios({
          method: 'post',
          url: API_URL + 'signIn/',
          data: {
            username: this.username,
            password: this.password
          },
          auth: {
            username: 'admin',
            password: '12345'
          }
        }).then((response) => {
         console.log(response);
         if(response.data.status=="success")
         {
         this.$router.push({path: '/dashboard'});
         this.$store.commit("setAuthentication", true);
         this.$store.commit("setUser", response.data.user);
         window.location.reload();
         }
         else
         {
           alert(response.data.message);
         }
         



        }).catch((error) => {
          console.log(error)
        })
      }
    },

    signUp() {
      this.username = document.getElementById('signUp_username').value;
      this.password = document.getElementById('signUp_password').value;
      var select = document.getElementById('signUp_type');
      this.userType = select.options[select.selectedIndex].value;
      if (this.username && this.password && this.userType) {
        axios({
          method: 'post',
          url: API_URL + 'signUp/',
          data: {
            username: this.username,
            password: this.password,
            type:this.userType
          },
          auth: {
            username: 'admin',
            password: '12345'
          }
        }).then((response) => {
          if(response.data.status=='success')
          {
            alert(response.data.message);
            this.step--;
            }
          else
            alert(response.data.message);

          console.log(response);

        }).catch((error) => {
          console.log(error)
        })
      }
    },


  }
};
</script>
