/*------------------------------GRABING ALL OUR GLOBAL VARIABLES------------------ */
const keys = document.querySelectorAll('.key');
const display_input = document.querySelector('.display .input');
const display_output = document.querySelector('.display .output');

let input ="";
/*---------------------DISPLAYING OPERATION SIGN ON CALCULATOR SCREEN---------------- */
for(let key of keys){
    const value = key.dataset.key;
    key.addEventListener('click', function(){
        //-----------------------------CHECKING CLEAR------------------------------------
          if(value =="clear"){
            input="";
            display_input.innerHTML="";
            display_output.innerHTML="";
        //--------------------------------CHECKING BACKSPACE ------------------------------
          }else if(value=="backspace"){ 
             input=input.slice(0, -1);
             display_input.innerHTML=CleanInput(input);
        //---------------------GETTING EVALUATED VALUES ON CALCULATOR SCREEN ------------------------------
         }else if (value=="="){
            let result = eval(input);
            display_output.innerHTML= CleanOutput(result);
        //------------------------CHECKING BRACKET ORIENTATION ON CALCULATIONS----------------------------------
         }else if (value=="brackets"){
            if (input.indexOf("(") == -1 ||
                input.indexOf("(") != -1 &&
                input.indexOf(")") != -1 && 
                input.lastIndexOf("(") < input.lastIndexOf(")")
                )
                {
                input += "(";
            }else if(input.indexOf("(") != -1 &&
                     input.indexOf(")") ==-1||
                     input.indexOf("(") != -1&&
                     input.indexOf(")") != -1&&
                     input.lastIndexOf("(") > input.lastIndexOf(")")     
                     )
                     {
                input += ")";
            }

            display_input.innerHTML=CleanInput(input);
         }else{
            if(ValidateInput(value)){  
            input+=value;
            display_input.innerHTML =CleanInput(input);
          }
         }
     })
} 
/*----------------------CLEANING THE INPUT THAT IS GIVING OPERANDS ON THE CALCULATOR SCXREEN--------------------- */
function CleanInput(input){
         let input_array = input.split("");
         let input_array_length = input_array.length;

         for (let i=0; i < input_array_length; i++){
               if (input_array[i] == "*"){
                input_array[i] = ' <span class="operator">x </span>';
               }else if (input_array[i] =="/"){
                input_array[i] = ' <span class="operator">÷</span>';
            }else if (input_array[i] =="+"){
                input_array[i] = ' <span class="operator">+</span>';
            }else if (input_array[i] =="-"){
                input_array[i] = ' <span class="operator">-</span>';
            }else if (input_array[i] =="("){
                input_array[i] = ' <span class="brackets">(</span>';
            }else if (input_array[i] ==")"){
                input_array[i] = '  <span class="brackets">)</span>';
            }
            else if (input_array[i] =="%"){
                input_array[i] = '<span class="percent">%</span>';
            }
        }
        return input_array.join("");
}
/*---------------------CLEANING THE OUTPUT SUCH AS PLACING A COMMA AFTER EVERY THREE DIGITS------------------ */
function CleanOutput(output){
    let output_string = output.toString();
    let decimal = output_string.split(".")[1];
    output_string = output_string.split(".")[0];

    let output_array = output_string.split("");

    let output_array_length = output_array.length;
    if(output_array.length > 3){
        for (let i =output_array.length - 3;i > 0; i -= 3) {
                   output_array.splice(i,0 , ",");
        }
    }

     if(decimal){
        output_array.push(".");
        output_array.push(decimal);
     }
  return output_array.join("");
     }

/*-----------------------VALIDATING INPUT ON CALCULATOR ON THE INPUT SECTION-----------------------------*/
     function ValidateInput(value){
        let last_input = input.slice(-1);
        let operators = ["+", "-" , "*" , "/"];

        if(value == "." && last_input == "."){
            return false;
        }
        if(operators.includes(value)){
            if(operators.includes(last_input)){
                return false;
              }else{
                return true;
              }
        }
          
        return true
   }

   
