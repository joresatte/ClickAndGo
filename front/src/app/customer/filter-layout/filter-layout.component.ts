import { Component, EventEmitter, Input, OnInit, Output, ViewChild } from '@angular/core';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatCardModule} from '@angular/material/card';
import {MatListModule} from '@angular/material/list';
import {MatMenuModule, MatMenuTrigger} from '@angular/material/menu';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatInputModule} from '@angular/material/input';
import {MatTabsModule} from '@angular/material/tabs';
import { FormsModule } from '@angular/forms';
import { DialogAnimationsExample } from '../../dialog/dialog.animations-example';
import {MatDialog} from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Constant } from '../../service/constant';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-filter-layout',
  standalone: true,
  imports: [MatGridListModule, MatCardModule, MatTabsModule,
            MatListModule,MatInputModule,
            MatMenuModule, MatIconModule, MatButtonModule, FormsModule, CommonModule],
  templateUrl: './filter-layout.component.html',
  styleUrl: './filter-layout.component.css'
})
export class FilterLayoutComponent implements OnInit{

  @Output()
  onChanged= new EventEmitter<string>()
  inputText:string= ''
  @Input()
  layout!:string
  listBtnClass= ''
  gribtnClass=''
  @Input()
  currentPage:string= Constant.currentPage
  otherPage:string=''
  @Output()
  sendactiveGrid= new EventEmitter<string>()
  @ViewChild('menuTrigger') menuTrigger!: MatMenuTrigger;
  activeShowGrid() {
    console.log('clicked')
    this.layout= 'grid'
    this.sendactiveGrid.emit(this.layout)
    this.gribtnClass='gribtnClass'
    this.listBtnClass=''
  }
  @Output()
  sendactiveList= new EventEmitter<string>()
  constructor(private dialog: MatDialog, private router: Router) {}
  getBack() {
    console.log('clicked')
    this.router.navigate(['/optionPage'])
  }
  ngOnInit(): void {
    this.currentPage=='pendingPage'? this.otherPage= 'Delivered Page': this.otherPage= 'Pending Page'
  }
 
  openDialog(enterAnimationDuration: string, exitAnimationDuration: string): void {
    this.dialog.open(DialogAnimationsExample, {
      width: '250px',
      enterAnimationDuration,
      exitAnimationDuration,
    });
  }
  openMenu(){
    const dialogRef = this.dialog.open(FilterLayoutComponent, {restoreFocus: false});
    dialogRef.afterClosed().subscribe(() => this.menuTrigger.focus());
  }
  reloadPage(){
    location.reload()
  }
  toPage(){
    this.otherPage=='Delivered Page'? this.router.navigate(['/deliveredPage']):this.router.navigate(['/pendingPage'])
    
  }
  cambiaLado(valor: any){
    this.inputText= valor
    this.onChanged.emit(this.inputText)
  }
  
}
