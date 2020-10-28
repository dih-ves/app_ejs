package br.com.ejs.projeto.integrador

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.SystemClock
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.login.*
import android.widget.Toast.makeText as makeText1

class MainActivity : DebugActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.login)

        campoImagem.setImageResource(R.drawable.logo_ejs)

        mensagemInicial.setText(R.string.mensagem_inicial)

        botaoLogin.setOnClickListener {

            progress.visibility = View.VISIBLE
            Handler().postDelayed(
                {

                    progress.visibility = View.GONE
                    val nomeUsuario = campoUsuario.text.toString()
                    val senha = campoSenha.text.toString()

                    //Toast.makeText(this, "Olá $nomeUsuario", Toast.LENGTH_LONG).show()

                    var intent = Intent(this, TelaInicialActivity::class.java)

//            var params = Bundle()
//            params.putString("nome_usuario", nomeUsuario)
//            params.putInt("numero", 10)
//
//            intent.putExtra(params)

                    intent.putExtra("nome_usuario", nomeUsuario)
                    intent.putExtra("number", 10)


                    startActivityForResult(intent, 0)
                }, 1000
            )
        }

        //override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
          //  super.onActivityResult(requestCode, resultCode, data)
            //campoUsuario.setText("")
            //campoSenha.setText("")
            //}
        }
    }
