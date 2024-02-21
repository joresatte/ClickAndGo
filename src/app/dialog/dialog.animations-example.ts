import { Component } from '@angular/core';
import {
  MatDialogRef,
  MatDialogActions,
  MatDialogClose,
  MatDialogContent,
} from '@angular/material/dialog';
import {MatButtonModule} from '@angular/material/button';
@Component({
  selector: 'dialog-animations-example',
  standalone: true,
  imports: [MatButtonModule, MatDialogActions, MatDialogClose, MatDialogContent],
  templateUrl: './dialog.animations-example.html',
  styleUrl: './dialog.animations-example.css'
})
export class DialogAnimationsExample { 

  constructor(public dialogRef: MatDialogRef<DialogAnimationsExample>) {}
  
}
