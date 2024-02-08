import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-intro',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './intro.component.html',
  styleUrl: './intro.component.css'
})
export class IntroComponent implements OnInit{

  eroski= 'Contigo'
  showContigo:boolean= false
  showIntro:boolean= true
  styleObject= {
    color: 'white',
    fontSize: '1em',
    backgroundColor:'',
    fontFamily:'cursive'
  }
  constructor(private router: Router){

  }
  ngOnInit(): void {
    setTimeout(()=>{
      this.showIntro= false
      this.router.navigate(['/loginPage'])
      console.log('router',this.router)
    }, 8000)
    setTimeout(()=>{
      this.showContigo= true
      this.styleObject.color= '#021691';
      this.styleObject.fontSize= '2em';
      this.styleObject.fontFamily= 'cursive'
    }, 3000)
  }
}
