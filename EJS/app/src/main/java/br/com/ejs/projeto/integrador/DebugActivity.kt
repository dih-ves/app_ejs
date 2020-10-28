package br.com.ejs.projeto.integrador

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.core.view.GravityCompat
import androidx.drawerlayout.widget.DrawerLayout
import com.google.android.material.navigation.NavigationView
import kotlinx.android.synthetic.main.toolbar.*


open class  DebugActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener  {

    private val TAG = "EJSApp"
    private val className: String
        get(){
            var s = javaClass.name
            return s.substring(s.lastIndexOf("."))
        }

    var drawerLayout: DrawerLayout? = null
    var navView: NavigationView? = null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d(TAG, "$className onCreat() executado")
    }

    protected fun configuraMenuLateral(){
        var toogle = ActionBarDrawerToggle(
            this,
            drawerLayout,
            toolbar_view,
            R.string.navigation_drawer_open,
            R.string.navigation_drawer_close
        )
        drawerLayout?.addDrawerListener(toogle)
        toogle.syncState()

        navView?.setNavigationItemSelectedListener(this)
    }


    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        when(item.itemId){
            R.id.nav_agenda -> {
                var intent = Intent(this, AgendaActivity::class.java)
                startActivity(intent)
            }
            R.id.nav_check -> {
                var intent = Intent(this, CheckInOut::class.java)
                startActivity(intent)
            }
            R.id.nav_mensagens -> {
                Toast.makeText(this, "Clicou em mensagens", Toast.LENGTH_LONG).show()
            }
        }

        drawerLayout?.closeDrawer(GravityCompat.START)

        return true
    }


    override fun onStart() {
        super.onStart()
        Log.d(TAG, "className onStart() executado")
    }

    override fun onResume() {
        super.onResume()
        Log.d(TAG, "className onResume() executado")
    }

    override fun onRestart() {
        super.onRestart()
        Log.d(TAG, "className onRestart() executado")
    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, "className onStop() executado")
    }
}